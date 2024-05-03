import os
import json
import fnmatch
from distinctipy import get_colors, get_hex
from django.contrib.gis.geos import GEOSGeometry, MultiPolygon
from django.core.management.base import BaseCommand
from django.db import connection
from seshat.apps.core.models import VideoShapefile

class Command(BaseCommand):
    help = 'Populates the database with Shapefiles'

    def add_arguments(self, parser):
        parser.add_argument('dir', type=str, help='Directory containing geojson files')

    def handle(self, *args, **options):
        dir = options['dir']

        # Clear the VideoShapefile table
        self.stdout.write(self.style.SUCCESS('Clearing VideoShapefile table...'))
        VideoShapefile.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('VideoShapefile table cleared'))

        # Get the start and end years for each shape
        # Load a file with 'name_years.json' in the filename kept in the same dir as the geojson files.
        # Loads a dict of polity names and their start and end years.
        # The values are lists of the form [[first_start_year, first_end_year], [second_start_year, second_end_year], ...]

        # List all files in the directory
        files = os.listdir(dir)

        # Find the first file that includes 'name_years.json' in the filename
        name_years_file = next((f for f in files if fnmatch.fnmatch(f, '*name_years.json*')), None)

        if name_years_file:
            name_years_path = os.path.join(dir, name_years_file)
            with open(name_years_path, 'r') as f:
                name_years = json.load(f)
        else:
            self.stdout.write(self.style.ERROR("No file found with 'name_years.json' in the filename"))

        # Dict of all the shape years for a given polity
        polity_years = {}
        # Set of all polities, for generating colour mapping
        all_polities = set()
        # Dict of all the polities found and the shapes they include
        polity_shapes = {}
        # Iterate over files in the directory
        for filename in os.listdir(dir):
            if filename.endswith('.geojson'):
                file_path = os.path.join(dir, filename)

                # Read and parse the GeoJSON file
                with open(file_path, 'r') as geojson_file:
                    geojson_data = json.load(geojson_file)

                # Extract data and create VideoShapefile instances
                for feature in geojson_data['features']:
                    properties = feature['properties']
                    if properties['Type'] == 'POLITY':
                        polity_name = properties['Name'].replace('(', '').replace(')', '')  # Remove spaces and brackets from name
                        polity_colour_key = polity_name
                        try:
                            if properties['Components']:
                                # If a shape has components we'll load the components instead
                                # Unless the components have their own components, then load the top level component
                                if len(properties['Components']) > 0 and '(' not in properties['Components']:
                                    polity_name = None
                        except KeyError:
                            pass

                        try:
                            if properties['Member_of']:
                                # If a shape is a component, get the parent polity to use as the polity_colour_key
                                if len(properties['Member_of']) > 0:
                                    polity_colour_key = polity_colour_key + ' - ' + properties['Member_of'].replace('(', '').replace(')', '')
                        except KeyError:
                            pass

                        # Save the years so we can determine the end year
                        if polity_name:
                            if polity_name not in polity_years:
                                polity_years[polity_name] = []
                            polity_years[polity_name].append(properties['Year'])
                            if polity_name not in polity_shapes:
                                polity_shapes[polity_name] = {}
                                polity_shapes[polity_name]['features'] = []
                                polity_shapes[polity_name]['colour_key'] = polity_colour_key
                            polity_shapes[polity_name]['features'].append(feature)

                            all_polities.add(polity_colour_key)

                            self.stdout.write(self.style.SUCCESS(f'Found shape for {polity_name} ({properties["Year"]})'))

        # Sort the polities and generate a colour mapping
        unique_polities = sorted(all_polities)
        self.stdout.write(self.style.SUCCESS(f'Generating colour mapping for {len(unique_polities)} polities'))
        pol_col_map = polity_colour_mapping(unique_polities)
        self.stdout.write(self.style.SUCCESS(f'Colour mapping generated'))

        # Iterate through polity_shapes and create VideoShapefile instances
        for polity_name, all_shapes_features in polity_shapes.items():
            features = all_shapes_features['features']
            polity_colour_key = all_shapes_features['colour_key']
            for feature in features:
                properties = feature['properties']
                self.stdout.write(self.style.SUCCESS(f'Importing shape for {polity_name} ({properties["Year"]})'))
                
                # Get a sorted list of the shape years this polity
                this_polity_years = sorted(polity_years[polity_name])

                # Get the polity start and end years
                polity_start_year = this_polity_years[0]
                polity_end_year = this_polity_years[-1]

                # Get the end year for a shape    
                # Most of the time, the shape end year is the year of the next shape
                # Some polities have a gap in their active years
                # For a shape year at the start of a gap, set the end year to be the shape year, so it doesn't cover the inactive period
                start_end_years = name_years[properties['Name']]
                end_years = [x[1] for x in start_end_years]
                if properties['Year'] in end_years:
                    end_year = properties['Year']
                else:
                    this_year_index = this_polity_years.index(properties['Year'])
                    try:
                        end_year = this_polity_years[this_year_index + 1] - 1
                    except IndexError:
                        end_year = polity_end_year
                
                # Save geom and convert Polygon to MultiPolygon if necessary
                geom = GEOSGeometry(json.dumps(feature['geometry']))
                if geom.geom_type == 'Polygon':
                    geom = MultiPolygon(geom)

                VideoShapefile.objects.create(
                    geom=geom,
                    name=polity_name,
                    polity=polity_colour_key,
                    wikipedia_name=properties['Wikipedia'],
                    seshat_id=properties['SeshatID'],
                    area=properties['Area_km2'],
                    start_year=properties['Year'],
                    end_year=end_year,
                    polity_start_year=polity_start_year,
                    polity_end_year=polity_end_year,
                    colour=pol_col_map[polity_colour_key]
                )

                self.stdout.write(self.style.SUCCESS(f'Successfully imported shape for {properties["Name"]} ({properties["Year"]})'))

            self.stdout.write(self.style.SUCCESS(f'Successfully imported all shapes for {polity_name}'))

        self.stdout.write(self.style.SUCCESS(f'Successfully imported all data from {filename}'))

        self.stdout.write(self.style.SUCCESS('Adding simplified geometries for faster loading...'))
        # Adjust the tolerance param of ST_Simplify as needed
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE core_videoshapefile 
                SET simplified_geom = ST_Simplify(geom, 0.07);
            """)
        self.stdout.write(self.style.SUCCESS('Simplified geometries added'))


def polity_colour_mapping(polities):
    """Use DistinctiPy package to assign a colour to each polity"""
    colours = []
    for col in get_colors(len(polities)):
        colours.append(get_hex(col))
    return dict(zip(polities, colours))
