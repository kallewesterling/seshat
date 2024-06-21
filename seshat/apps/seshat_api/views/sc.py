from rest_framework import viewsets

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from ._mixins import (
    MixinSeshatAPIAuth,
    MixinSeshatAPISerializer,
    SeshatAPIPagination,
)

from ...sc.models import (
    Ra,
    Polity_territory,
    Polity_population,
    Population_of_the_largest_settlement,
    Settlement_hierarchy,
    Administrative_level,
    Religious_level,
    Military_level,
    Professional_military_officer,
    Professional_soldier,
    Professional_priesthood,
    Full_time_bureaucrat,
    Examination_system,
    Merit_promotion,
    Specialized_government_building,
    Formal_legal_code,
    Judge,
    Court,
    Professional_lawyer,
    Irrigation_system,
    Drinking_water_supply_system,
    Market,
    Food_storage_site,
    Road,
    Bridge,
    Canal,
    Port,
    Mines_or_quarry,
    Mnemonic_device,
    Nonwritten_record,
    Written_record,
    Script,
    Non_phonetic_writing,
    Phonetic_alphabetic_writing,
    Lists_tables_and_classification,
    Calendar,
    Sacred_text,
    Religious_literature,
    Practical_literature,
    History,
    Philosophy,
    Scientific_literature,
    Fiction,
    Article,
    Token,
    Precious_metal,
    Foreign_coin,
    Indigenous_coin,
    Paper_currency,
    Courier,
    Postal_station,
    General_postal_service,
    Communal_building,
    Utilitarian_public_building,
    Symbolic_building,
    Entertainment_building,
    Knowledge_or_information_building,
    Other_utilitarian_public_building,
    Special_purpose_site,
    Ceremonial_site,
    Burial_site,
    Trading_emporia,
    Enclosure,
    Length_measurement_system,
    Area_measurement_system,
    Volume_measurement_system,
    Weight_measurement_system,
    Time_measurement_system,
    Geometrical_measurement_system,
    Other_measurement_system,
    Debt_and_credit_structure,
    Store_of_wealth,
    Source_of_support,
    Occupational_complexity,
    Special_purpose_house,
    Other_special_purpose_site,
    Largest_communication_distance,
    Fastest_individual_communication,
)


class RAViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing RAs.
    """
    model = Ra
    pagination_class = SeshatAPIPagination


class PolityTerritoryViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Polity Territories.
    """
    model = Polity_territory
    pagination_class = SeshatAPIPagination


class PolityPopulationViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Polity Populations.
    """
    model = Polity_population
    pagination_class = SeshatAPIPagination


class PopulationOfTheLargestSettlementViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Population of the Largest Settlements.
    """
    model = Population_of_the_largest_settlement
    pagination_class = SeshatAPIPagination


class SettlementHierarchyViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Settlement Hierarchies.
    """
    model = Settlement_hierarchy
    pagination_class = SeshatAPIPagination


class AdministrativeLevelViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Administrative Levels.
    """
    model = Administrative_level
    pagination_class = SeshatAPIPagination


class ReligiousLevelViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Religious Levels.
    """
    model = Religious_level
    pagination_class = SeshatAPIPagination


class MilitaryLevelViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Military Levels.
    """
    model = Military_level
    pagination_class = SeshatAPIPagination


class ProfessionalMilitaryOfficerViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Professional Military Officers.
    """
    model = Professional_military_officer
    pagination_class = SeshatAPIPagination


class ProfessionalSoldierViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Professional Soldiers.
    """
    model = Professional_soldier
    pagination_class = SeshatAPIPagination


class ProfessionalPriesthoodViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Professional Priesthoods.
    """
    model = Professional_priesthood
    pagination_class = SeshatAPIPagination


class FullTimeBureaucratViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Full Time Bureaucrats.
    """
    model = Full_time_bureaucrat
    pagination_class = SeshatAPIPagination


class ExaminationSystemViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Examination Systems.
    """
    model = Examination_system
    pagination_class = SeshatAPIPagination


class MeritPromotionViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Merit Promotions.
    """
    model = Merit_promotion
    pagination_class = SeshatAPIPagination


class SpecializedGovernmentBuildingViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Specialized Government Buildings.
    """
    model = Specialized_government_building
    pagination_class = SeshatAPIPagination


class FormalLegalCodeViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Formal Legal Codes.
    """
    model = Formal_legal_code
    pagination_class = SeshatAPIPagination


class JudgeViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Judges.
    """
    model = Judge
    pagination_class = SeshatAPIPagination


class CourtViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Courts.
    """
    model = Court
    pagination_class = SeshatAPIPagination


class ProfessionalLawyerViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Professional Lawyers.
    """
    model = Professional_lawyer
    pagination_class = SeshatAPIPagination


class IrrigationSystemViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Irrigation Systems.
    """
    model = Irrigation_system
    pagination_class = SeshatAPIPagination


class DrinkingWaterSupplySystemViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Drinking Water Supply Systems.
    """
    model = Drinking_water_supply_system
    pagination_class = SeshatAPIPagination


class MarketViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Markets.
    """
    model = Market
    pagination_class = SeshatAPIPagination


class FoodStorageSiteViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Food Storage Sites.
    """
    model = Food_storage_site
    pagination_class = SeshatAPIPagination


class RoadViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Roads.
    """
    model = Road
    pagination_class = SeshatAPIPagination


class BridgeViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Bridges.
    """
    model = Bridge
    pagination_class = SeshatAPIPagination


class CanalViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Canals.
    """
    model = Canal
    pagination_class = SeshatAPIPagination


class PortViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Ports.
    """
    model = Port
    pagination_class = SeshatAPIPagination


class MinesOrQuarryViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Mines or Quarries.
    """
    model = Mines_or_quarry
    pagination_class = SeshatAPIPagination


class MnemonicDeviceViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Mnemonic Devices.
    """
    model = Mnemonic_device
    pagination_class = SeshatAPIPagination


class NonwrittenRecordViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Nonwritten Records.
    """
    model = Nonwritten_record
    pagination_class = SeshatAPIPagination


class WrittenRecordViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Written Records.
    """
    model = Written_record
    pagination_class = SeshatAPIPagination


class ScriptViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Scripts.
    """
    model = Script
    pagination_class = SeshatAPIPagination


class NonPhoneticWritingViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Non-Phonetic Writings.
    """
    model = Non_phonetic_writing
    pagination_class = SeshatAPIPagination


class PhoneticAlphabeticWritingViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Phonetic Alphabetic Writings.
    """
    model = Phonetic_alphabetic_writing
    pagination_class = SeshatAPIPagination


class ListsTablesAndClassificationViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Lists, Tables, and Classifications.
    """
    model = Lists_tables_and_classification
    pagination_class = SeshatAPIPagination


class CalendarViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Calendars.
    """
    model = Calendar
    pagination_class = SeshatAPIPagination


class SacredTextViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Sacred Texts.
    """
    model = Sacred_text
    pagination_class = SeshatAPIPagination


class ReligiousLiteratureViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Religious Literatures.
    """
    model = Religious_literature
    pagination_class = SeshatAPIPagination


class PracticalLiteratureViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Practical Literatures.
    """
    model = Practical_literature
    pagination_class = SeshatAPIPagination


class HistoryViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Histories.
    """
    model = History
    pagination_class = SeshatAPIPagination


class PhilosophyViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Philosophies.
    """
    model = Philosophy
    pagination_class = SeshatAPIPagination


class ScientificLiteratureViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Scientific Literatures.
    """
    model = Scientific_literature
    pagination_class = SeshatAPIPagination


class FictionViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Fictions.
    """
    model = Fiction
    pagination_class = SeshatAPIPagination


class ArticleViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Articles.
    """
    model = Article
    pagination_class = SeshatAPIPagination


class TokenViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Tokens.
    """
    model = Token
    pagination_class = SeshatAPIPagination


class PreciousMetalViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Precious Metals.
    """
    model = Precious_metal
    pagination_class = SeshatAPIPagination


class ForeignCoinViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Foreign Coins.
    """
    model = Foreign_coin
    pagination_class = SeshatAPIPagination


class IndigenousCoinViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Indigenous Coins.
    """
    model = Indigenous_coin
    pagination_class = SeshatAPIPagination


class PaperCurrencyViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Paper Currencies.
    """
    model = Paper_currency
    pagination_class = SeshatAPIPagination


class CourierViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Couriers.
    """
    model = Courier
    pagination_class = SeshatAPIPagination


class PostalStationViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Postal Stations.
    """
    model = Postal_station
    pagination_class = SeshatAPIPagination


class GeneralPostalServiceViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing General Postal Services.
    """
    model = General_postal_service
    pagination_class = SeshatAPIPagination


class CommunalBuildingViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Communal Buildings.
    """
    model = Communal_building
    pagination_class = SeshatAPIPagination


class UtilitarianPublicBuildingViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Utilitarian Public Buildings.
    """
    model = Utilitarian_public_building
    pagination_class = SeshatAPIPagination


class SymbolicBuildingViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Symbolic Buildings.
    """
    model = Symbolic_building
    pagination_class = SeshatAPIPagination


class EntertainmentBuildingViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Entertainment Buildings.
    """
    model = Entertainment_building
    pagination_class = SeshatAPIPagination


class KnowledgeOrInformationBuildingViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Knowledge or Information Buildings.
    """
    model = Knowledge_or_information_building
    pagination_class = SeshatAPIPagination


class OtherUtilitarianPublicBuildingViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Other Utilitarian Public Buildings.
    """
    model = Other_utilitarian_public_building
    pagination_class = SeshatAPIPagination


class SpecialPurposeSiteViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Special Purpose Sites.
    """
    model = Special_purpose_site
    pagination_class = SeshatAPIPagination


class CeremonialSiteViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Ceremonial Sites.
    """
    model = Ceremonial_site
    pagination_class = SeshatAPIPagination


class BurialSiteViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Burial Sites.
    """
    model = Burial_site
    pagination_class = SeshatAPIPagination


class TradingEmporiaViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Trading Emporias.
    """
    model = Trading_emporia
    pagination_class = SeshatAPIPagination


class EnclosureViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Enclosures.
    """
    model = Enclosure
    pagination_class = SeshatAPIPagination


class LengthMeasurementSystemViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Length Measurement Systems.
    """
    model = Length_measurement_system
    pagination_class = SeshatAPIPagination


class AreaMeasurementSystemViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Area Measurement Systems.
    """
    model = Area_measurement_system
    pagination_class = SeshatAPIPagination


class VolumeMeasurementSystemViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Volume Measurement Systems.
    """
    model = Volume_measurement_system
    pagination_class = SeshatAPIPagination


class WeightMeasurementSystemViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Weight Measurement Systems.
    """
    model = Weight_measurement_system
    pagination_class = SeshatAPIPagination


class TimeMeasurementSystemViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Time Measurement Systems.
    """
    model = Time_measurement_system
    pagination_class = SeshatAPIPagination


class GeometricalMeasurementSystemViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Geometrical Measurement Systems.
    """
    model = Geometrical_measurement_system
    pagination_class = SeshatAPIPagination


class OtherMeasurementSystemViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Other Measurement Systems.
    """
    model = Other_measurement_system
    pagination_class = SeshatAPIPagination


class DebtAndCreditStructureViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Debt and Credit Structures.
    """
    model = Debt_and_credit_structure
    pagination_class = SeshatAPIPagination


class StoreOfWealthViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Stores of Wealth.
    """
    model = Store_of_wealth
    pagination_class = SeshatAPIPagination


class SourceOfSupportViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Sources of Support.
    """
    model = Source_of_support
    pagination_class = SeshatAPIPagination


class OccupationalComplexityViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Occupational Complexities.
    """
    model = Occupational_complexity
    pagination_class = SeshatAPIPagination


class SpecialPurposeHouseViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Special Purpose Houses.
    """
    model = Special_purpose_house
    pagination_class = SeshatAPIPagination


class OtherSpecialPurposeSiteViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Other Special Purpose Sites.
    """
    model = Other_special_purpose_site
    pagination_class = SeshatAPIPagination


class LargestCommunicationDistanceViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Largest Communication Distances.
    """
    model = Largest_communication_distance
    pagination_class = SeshatAPIPagination


class FastestIndividualCommunicationViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Fastest Individual Communications.
    """
    model = Fastest_individual_communication
    pagination_class = SeshatAPIPagination
