# Generated by Django 4.0.3 on 2024-02-22 11:06

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_gadmcountries_gadmprovinces_gadmshapefile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoshapefile',
            name='simplified_geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326),
        ),
    ]