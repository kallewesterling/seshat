from rest_framework import viewsets

from ._mixins import (
    MixinSeshatAPIAuth,
    MixinSeshatAPISerializer,
    SeshatAPIPagination,
)

from ...crisisdb.models import (
    Us_location,
    Us_violence_subtype,
    Us_violence_data_source,
    Us_violence,
    Crisis_consequence,
    Power_transition,
    Human_sacrifice,
    External_conflict,
    Internal_conflict,
    External_conflict_side,
    Agricultural_population,
    Arable_land,
    Arable_land_per_farmer,
    Gross_grain_shared_per_agricultural_population,
    Net_grain_shared_per_agricultural_population,
    Surplus,
    Military_expense,
    Silver_inflow,
    Silver_stock,
    Total_population,
    Gdp_per_capita,
    Drought_event,
    Locust_event,
    Socioeconomic_turmoil_event,
    Crop_failure_event,
    Famine_event,
    Disease_outbreak,
)


class USLocationViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing US Locations.
    """
    model = Us_location
    pagination_class = SeshatAPIPagination


class USViolenceSubtypeViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing US Violence Subtypes.
    """
    model = Us_violence_subtype
    pagination_class = SeshatAPIPagination


class USViolenceDataSourceViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing US Violence Data Sources.
    """
    model = Us_violence_data_source
    pagination_class = SeshatAPIPagination


class USViolenceViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing US Violence.
    """
    model = Us_violence
    pagination_class = SeshatAPIPagination


class CrisisConsequenceViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Crisis Consequences.
    """
    model = Crisis_consequence
    pagination_class = SeshatAPIPagination


class PowerTransitionViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Power Transitions.
    """
    model = Power_transition
    pagination_class = SeshatAPIPagination


class HumanSacrificeViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Human Sacrifices.
    """
    model = Human_sacrifice
    pagination_class = SeshatAPIPagination


class ExternalConflictViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing External Conflicts.
    """
    model = External_conflict
    pagination_class = SeshatAPIPagination


class InternalConflictViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Internal Conflicts.
    """
    model = Internal_conflict
    pagination_class = SeshatAPIPagination


class ExternalConflictSideViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing External Conflict Sides.
    """
    model = External_conflict_side
    pagination_class = SeshatAPIPagination


class AgriculturalPopulationViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Agricultural Populations.
    """
    model = Agricultural_population
    pagination_class = SeshatAPIPagination


class ArableLandViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Arable Lands.
    """
    model = Arable_land
    pagination_class = SeshatAPIPagination


class ArableLandPerFarmerViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Arable Land Per Farmers.
    """
    model = Arable_land_per_farmer
    pagination_class = SeshatAPIPagination


class GrossGrainSharedPerAgriculturalPopulationViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Gross Grain Shared Per Agricultural Populations.
    """
    model = Gross_grain_shared_per_agricultural_population
    pagination_class = SeshatAPIPagination


class NetGrainSharedPerAgriculturalPopulationViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Net Grain Shared Per Agricultural Populations.
    """
    model = Net_grain_shared_per_agricultural_population
    pagination_class = SeshatAPIPagination


class SurplusViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Surpluses.
    """
    model = Surplus
    pagination_class = SeshatAPIPagination


class MilitaryExpenseViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Military Expenses.
    """
    model = Military_expense
    pagination_class = SeshatAPIPagination


class SilverInflowViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Silver Inflows.
    """
    model = Silver_inflow
    pagination_class = SeshatAPIPagination


class SilverStockViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Silver Stocks.
    """
    model = Silver_stock
    pagination_class = SeshatAPIPagination


class TotalPopulationViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Total Populations.
    """
    model = Total_population
    pagination_class = SeshatAPIPagination


class GDPPerCapitaViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing GDP Per Capitas.
    """
    model = Gdp_per_capita
    pagination_class = SeshatAPIPagination


class DroughtEventViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Drought Events.
    """
    model = Drought_event
    pagination_class = SeshatAPIPagination


class LocustEventViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Locust Events.
    """
    model = Locust_event
    pagination_class = SeshatAPIPagination


class SocioeconomicTurmoilEventViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Socioeconomic Turmoil Events.
    """
    model = Socioeconomic_turmoil_event
    pagination_class = SeshatAPIPagination


class CropFailureEventViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Crop Failure Events.
    """
    model = Crop_failure_event
    pagination_class = SeshatAPIPagination


class FamineEventViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Famine Events.
    """
    model = Famine_event
    pagination_class = SeshatAPIPagination


class DiseaseOutbreakViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Disease Outbreaks.
    """
    model = Disease_outbreak
    pagination_class = SeshatAPIPagination
