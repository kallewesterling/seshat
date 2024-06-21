from django.urls import path, include
from rest_framework import routers

from . import views  # temp -- remove

# Create router for URLS
router = routers.DefaultRouter()


# Register viewsets for "account" app
from .views.accounts import (
    ProfileViewSet,
    SeshatExpertViewSet,
    SeshatTaskViewSet,
)

router.register(r"profiles", ProfileViewSet, basename="profile")
router.register(
    r"seshat-experts",
    SeshatExpertViewSet,
    basename="seshat-expert",
)
router.register(r"seshat-tasks", SeshatTaskViewSet, basename="seshat-task")


# Register views for "core" app

from .views.core import (
    PrivateCommentsViewSet,
    PrivateCommentsPartsViewSet,
    MacroRegionViewSet,
    RegionViewSet,
    NGAViewSet,
    PolityViewSet,
    CapitalViewSet,
    NGAPolityRelationsViewSet,
    CountryViewSet,
    SectionViewSet,
    SubsectionViewSet,
    VariableHierarchyViewSet,
    ReferenceViewSet,
    CitationViewSet,
    SeshatCommentViewSet,
    SeshatCommentPartViewSet,
    ScpThroughCtnViewSet,
    SeshatCommonViewSet,
    ReligionViewSet,
    VideoShapefileViewSet,
    GADMShapefileViewSet,
    GADMCountriesViewSet,
    GADMProvincesViewSet,
)

router.register(
    r"private-comments",
    PrivateCommentsViewSet,
    basename="private-comment",
)
router.register(
    r"private-comments-parts",
    PrivateCommentsPartsViewSet,
    basename="private-comment-part",
)
router.register(r"macro-regions", MacroRegionViewSet, basename="macro-region")
router.register(r"regions", RegionViewSet, basename="region")
router.register(r"ngas", NGAViewSet, basename="nga")
router.register(r"polities", PolityViewSet, basename="polity")
router.register(r"capitals", CapitalViewSet, basename="capital")
router.register(
    r"nga-polity-relations",
    NGAPolityRelationsViewSet,
    basename="nga-polity-relation",
)
router.register(r"countries", CountryViewSet, basename="country")
router.register(r"sections", SectionViewSet, basename="section")
router.register(r"subsections", SubsectionViewSet, basename="subsection")
router.register(
    r"variable-hierarchies",
    VariableHierarchyViewSet,
    basename="variable-hierarchy",
)
router.register(r"references", ReferenceViewSet, basename="reference")
router.register(r"citations", CitationViewSet, basename="citation")
router.register(r"comments", SeshatCommentViewSet, basename="seshat-comment")
router.register(
    r"comment-parts",
    SeshatCommentPartViewSet,
    basename="seshat-comment-part",
)
router.register(
    r"comment-parts-through-citations",
    ScpThroughCtnViewSet,
    basename="comment-part-through-citation",
)
router.register(r"commons", SeshatCommonViewSet, basename="common")
router.register(r"religions", ReligionViewSet, basename="religion")
router.register(
    r"video-shapefiles",
    VideoShapefileViewSet,
    basename="video-shapefile",
)
router.register(
    r"gadm-shapefiles",
    GADMShapefileViewSet,
    basename="gadm-shapefile",
)
router.register(
    r"gadm-countries", GADMCountriesViewSet, basename="gadm-country"
)
router.register(
    r"gadm-provinces",
    GADMProvincesViewSet,
    basename="gadm-province",
)


# Register views for "crisisdb" app

from .views.crisisdb import (
    USLocationViewSet,
    USViolenceSubtypeViewSet,
    USViolenceDataSourceViewSet,
    USViolenceViewSet,
    CrisisConsequenceViewSet,
    PowerTransitionViewSet,
    HumanSacrificeViewSet,
    ExternalConflictViewSet,
    ExternalConflictSideViewSet,
    AgriculturalPopulationViewSet,
    ArableLandViewSet,
    ArableLandPerFarmerViewSet,
    GrossGrainSharedPerAgriculturalPopulationViewSet,
    NetGrainSharedPerAgriculturalPopulationViewSet,
    SurplusViewSet,
    MilitaryExpenseViewSet,
    SilverInflowViewSet,
    SilverStockViewSet,
    TotalPopulationViewSet,
    GDPPerCapitaViewSet,
    DroughtEventViewSet,
    LocustEventViewSet,
    SocioeconomicTurmoilEventViewSet,
    CropFailureEventViewSet,
    FamineEventViewSet,
    DiseaseOutbreakViewSet,
)

router.register(r"us-locations", USLocationViewSet, basename="us-location")
router.register(
    r"us-violence-subtypes",
    USViolenceSubtypeViewSet,
    basename="us-violence-subtype",
)
router.register(
    r"us-violence-data-sources",
    USViolenceDataSourceViewSet,
    basename="us-violence-data-source",
)
router.register(r"us-violences", USViolenceViewSet, basename="us-violence")
router.register(
    r"crisis-consequences",
    CrisisConsequenceViewSet,
    basename="crisis-consequence",
)
router.register(
    r"power-transitions",
    PowerTransitionViewSet,
    basename="power-transition",
)

router.register(
    r"human-sacrifices",
    HumanSacrificeViewSet,
    basename="human-sacrifice",
)
router.register(
    r"external-conflicts",
    ExternalConflictViewSet,
    basename="external-conflict",
)
router.register(
    r"external-conflict-sides",
    ExternalConflictSideViewSet,
    basename="external-conflict-side",
)
router.register(
    r"agricultural-populations",
    AgriculturalPopulationViewSet,
    basename="agricultural-population",
)
router.register(r"arable-lands", ArableLandViewSet, basename="arable-land")
router.register(
    r"arable-land-per-farmer",
    ArableLandPerFarmerViewSet,
    basename="arable-land-per-farmer",
)
router.register(
    r"gross-grain-shared-per-agricultural-populations",
    GrossGrainSharedPerAgriculturalPopulationViewSet,
    basename="gross-grain-shared-per-agricultural-population",
)
router.register(
    r"net-grain-shared-per-agricultural-populations",
    NetGrainSharedPerAgriculturalPopulationViewSet,
    basename="net-grain-shared-per-agricultural-population",
)
router.register(r"surpluses", SurplusViewSet, basename="surplus")
router.register(
    r"military-expenses",
    MilitaryExpenseViewSet,
    basename="military-expense",
)
router.register(
    r"silver-inflows",
    SilverInflowViewSet,
    basename="silver-inflow",
)
router.register(
    r"silver-stocks",
    SilverStockViewSet,
    basename="silver-stock",
)
router.register(
    r"total-populations",
    TotalPopulationViewSet,
    basename="total-population",
)
router.register(
    r"gdp-per-capitas",
    GDPPerCapitaViewSet,
    basename="gdp-per-capita",
)
router.register(
    r"drought-events",
    DroughtEventViewSet,
    basename="drought-event",
)
router.register(
    r"locust-events",
    LocustEventViewSet,
    basename="locust-event",
)
router.register(
    r"socioeconomic-turmoil-events",
    SocioeconomicTurmoilEventViewSet,
    basename="socioeconomic-turmoil-event",
)
router.register(
    r"crop-failure-events",
    CropFailureEventViewSet,
    basename="crop-failure-event",
)
router.register(
    r"famine-events",
    FamineEventViewSet,
    basename="famine-event",
)
router.register(
    r"disease-outbreaks",
    DiseaseOutbreakViewSet,
    basename="disease-outbreak",
)


# app: general

from .views.general import (
    PolityResearchAssistantViewSet,
    PolityOriginalNameViewSet,
    PolityAlternativeNameViewSet,
    PolityDurationViewSet,
    PolityPeakYearsViewSet,
    PolityDegreeOfCentralizationViewSet,
    PolitySuprapolityRelationsViewSet,
    PolityUTMZoneViewSet,
    PolityCapitalViewSet,
    PolityLanguageViewSet,
    PolityLinguisticFamilyViewSet,
    PolityLanguageGenusViewSet,
    PolityReligionGenusViewSet,
    PolityReligionFamilyViewSet,
    PolityReligionViewSet,
    PolityRelationshipToPrecedingEntityViewSet,
    PolityPrecedingEntityViewSet,
    PolitySucceedingEntityViewSet,
    PolitySupraculturalEntityViewSet,
    PolityScaleOfSupraculturalInteractionViewSet,
    PolityAlternateReligionGenusViewSet,
    PolityAlternateReligionFamilyViewSet,
    PolityAlternateReligionViewSet,
    PolityExpertViewSet,
    PolityEditorViewSet,
    PolityReligiousTraditionViewSet,
)

router.register(
    r"polity-research-assistants",
    PolityResearchAssistantViewSet,
    basename="polity-research-assistant",
)
router.register(
    r"polity-original-names",
    PolityOriginalNameViewSet,
    basename="polity-original-name",
)
router.register(
    r"polity-alternative-names",
    PolityAlternativeNameViewSet,
    basename="polity-alternative-name",
)
router.register(
    r"polity-durations", PolityDurationViewSet, basename="polity-duration"
)
router.register(
    r"polity-peak-years", PolityPeakYearsViewSet, basename="polity-peak-years"
)
router.register(
    r"polity-degree-of-centralizations",
    PolityDegreeOfCentralizationViewSet,
    basename="polity-degree-of-centralization",
)
router.register(
    r"polity-suprapolities",
    PolitySuprapolityRelationsViewSet,
    basename="polity-suprapolity",
)
router.register(
    r"polity-utm-timezones",
    PolityUTMZoneViewSet,
    basename="polity-utm-timezone",
)
router.register(
    r"polity-capitals", PolityCapitalViewSet, basename="polity-capital"
)
router.register(
    r"polity-languages", PolityLanguageViewSet, basename="polity-language"
)
router.register(
    r"polity-linguistic-families",
    PolityLinguisticFamilyViewSet,
    basename="polity-linguistic-family",
)
router.register(
    r"polity-language-genuses",
    PolityLanguageGenusViewSet,
    basename="polity-language-genus",
)
router.register(
    r"polity-religion-genuses",
    PolityReligionGenusViewSet,
    basename="polity-religion-genus",
)
router.register(
    r"polity-religion-families",
    PolityReligionFamilyViewSet,
    basename="polity-religion-family",
)
router.register(
    r"polity-religions", PolityReligionViewSet, basename="polity-religion"
)
router.register(
    r"polity-relationship-to-preceding-entities",
    PolityRelationshipToPrecedingEntityViewSet,
    basename="polity-relationship-to-preceding-entity",
)
router.register(
    r"polity-preceding-entities",
    PolityPrecedingEntityViewSet,
    basename="polity-preceding-entity",
)
router.register(
    r"polity-succeeding-entities",
    PolitySucceedingEntityViewSet,
    basename="polity-succeeding-entity",
)
router.register(
    r"polity-supracultural-entities",
    PolitySupraculturalEntityViewSet,
    basename="polity-supracultural-entity",
)
router.register(
    r"polity-scale-of-supracultural-interactions",
    PolityScaleOfSupraculturalInteractionViewSet,
    basename="polity-scale-of-supracultural-interaction",
)
router.register(
    r"polity-alternate-religion-genuses",
    PolityAlternateReligionGenusViewSet,
    basename="polity-alternate-religion-genus",
)
router.register(
    r"polity-alternate-religion-families",
    PolityAlternateReligionFamilyViewSet,
    basename="polity-alternate-religion-family",
)
router.register(
    r"polity-alternate-religions",
    PolityAlternateReligionViewSet,
    basename="polity-alternate-religion",
)
router.register(
    r"polity-experts", PolityExpertViewSet, basename="polity-expert"
)
router.register(
    r"polity-editors", PolityEditorViewSet, basename="polity-editor"
)
router.register(
    r"polity-religious-traditions",
    PolityReligiousTraditionViewSet,
    basename="polity-religious-tradition",
)


# Register views for "rt" app

from .views.rt import (
    WidespreadReligionViewSet,
    OfficialReligionViewSet,
    ElitesReligionViewSet,
    TheoSyncDifRelViewSet,
    SyncRelPraIndBeliViewSet,
    ReligiousFragmentationViewSet,
    GovVioFreqRelGrpViewSet,
    GovResPubWorViewSet,
    GovResPubProsViewSet,
    GovResConvViewSet,
    GovPressConvViewSet,
    GovResPropOwnForRelGrpViewSet,
    TaxRelAdhActInsViewSet,
    GovOblRelGrpOfcRecoViewSet,
    GovResConsRelBuilViewSet,
    GovResRelEduViewSet,
    GovResCirRelLitViewSet,
    GovDisRelGrpOccFunViewSet,
    SocVioFreqRelGrpViewSet,
    SocDisRelGrpOccFunViewSet,
    GovPressConvForAgaViewSet,
)

router.register(
    r"widespread-religions",
    WidespreadReligionViewSet,
    basename="widespread-religion",
)
router.register(
    r"official-religions",
    OfficialReligionViewSet,
    basename="official-religion",
)
router.register(
    r"elites-religions", ElitesReligionViewSet, basename="elites-religion"
)
router.register(
    r"theological-syncretism-of-different-religions",
    TheoSyncDifRelViewSet,
    basename="theological-syncretism-of-different-religions",
)
router.register(
    r"syncretism-of-religious-practices-at-the-level-of-individual-believers",
    SyncRelPraIndBeliViewSet,
    basename="syncretism-of-religious-practices-at-the-level-of-individual-believers",
)
router.register(
    r"religious-fragmentations",
    ReligiousFragmentationViewSet,
    basename="religious-fragmentation",
)
router.register(
    r"frequency-of-governmental-violence-against-religious-groups",
    GovVioFreqRelGrpViewSet,
    basename="frequency-of-governmental-violence-against-religious-groups",
)
router.register(
    r"government-restrictions-on-public-worships",
    GovResPubWorViewSet,
    basename="government-restrictions-on-public-worships",
)
router.register(
    r"government-restrictions-on-public-proselytizings",
    GovResPubProsViewSet,
    basename="government-restrictions-on-public-proselytizings",
)
router.register(
    r"government-restrictions-on-conversions",
    GovResConvViewSet,
    basename="government-restrictions-on-conversions",
)
router.register(
    r"government-pressure-to-converts",
    GovPressConvViewSet,
    basename="government-pressure-to-converts",
)
router.register(
    r"government-restrictions-on-property-ownership-for-adherents-of-and-religious-groups",
    GovResPropOwnForRelGrpViewSet,
    basename="government-restrictions-on-property-ownership-for-adherents-of-and-religious-groups",
)
router.register(
    r"taxes-based-on-religious-adherence-or-on-religious-activities-and-institutions",
    TaxRelAdhActInsViewSet,
    basename="taxes-based-on-religious-adherence-or-on-religious-activities-and-institutions",
)
router.register(
    r"governmental-obligations-for-religious-groups-to-apply-for-official-recognitions",
    GovOblRelGrpOfcRecoViewSet,
    basename="governmental-obligations-for-religious-groups-to-apply-for-official-recognitions",
)
router.register(
    r"government-restrictions-on-construction-of-religious-buildings",
    GovResConsRelBuilViewSet,
    basename="government-restrictions-on-construction-of-religious-buildings",
)
router.register(
    r"government-restrictions-on-religious-educations",
    GovResRelEduViewSet,
    basename="government-restrictions-on-religious-educations",
)
router.register(
    r"government-restrictions-on-circulation-of-religious-literatures",
    GovResCirRelLitViewSet,
    basename="government-restrictions-on-circulation-of-religious-literatures",
)
router.register(
    r"government-discrimination-against-religious-groups-taking-up-certain-occupations-or-functions",
    GovDisRelGrpOccFunViewSet,
    basename="government-discrimination-against-religious-groups-taking-up-certain-occupations-or-functions",
)
router.register(
    r"frequency-of-societal-violence-against-religious-groups",
    SocVioFreqRelGrpViewSet,
    basename="frequency-of-societal-violence-against-religious-groups",
)
router.register(
    r"societal-discrimination-against-religious-groups-taking-up-certain-occupations-or-functions",
    SocDisRelGrpOccFunViewSet,
    basename="societal-discrimination-against-religious-groups-taking-up-certain-occupations-or-functions",
)
router.register(
    r"societal-pressure-to-convert-or-against-conversions",
    GovPressConvForAgaViewSet,
    basename="societal-pressure-to-convert-or-against-conversions",
)

# Add views for "sc" app to the router

from .views.sc import (
    RAViewSet,
    PolityTerritoryViewSet,
    PolityPopulationViewSet,
    PopulationOfTheLargestSettlementViewSet,
    SettlementHierarchyViewSet,
    AdministrativeLevelViewSet,
    ReligiousLevelViewSet,
    MilitaryLevelViewSet,
    ProfessionalMilitaryOfficerViewSet,
    ProfessionalSoldierViewSet,
    ProfessionalPriesthoodViewSet,
    FullTimeBureaucratViewSet,
    ExaminationSystemViewSet,
    MeritPromotionViewSet,
    SpecializedGovernmentBuildingViewSet,
    FormalLegalCodeViewSet,
    JudgeViewSet,
    CourtViewSet,
    ProfessionalLawyerViewSet,
    IrrigationSystemViewSet,
    DrinkingWaterSupplySystemViewSet,
    MarketViewSet,
    FoodStorageSiteViewSet,
    RoadViewSet,
    BridgeViewSet,
    CanalViewSet,
    PortViewSet,
    MinesOrQuarryViewSet,
    MnemonicDeviceViewSet,
    NonwrittenRecordViewSet,
    WrittenRecordViewSet,
    ScriptViewSet,
    NonPhoneticWritingViewSet,
    PhoneticAlphabeticWritingViewSet,
    ListsTablesAndClassificationViewSet,
    CalendarViewSet,
    SacredTextViewSet,
    ReligiousLiteratureViewSet,
    PracticalLiteratureViewSet,
    HistoryViewSet,
    PhilosophyViewSet,
    ScientificLiteratureViewSet,
    FictionViewSet,
    ArticleViewSet,
    TokenViewSet,
    PreciousMetalViewSet,
    ForeignCoinViewSet,
    IndigenousCoinViewSet,
    PaperCurrencyViewSet,
    CourierViewSet,
    PostalStationViewSet,
    GeneralPostalServiceViewSet,
    CommunalBuildingViewSet,
    UtilitarianPublicBuildingViewSet,
    SymbolicBuildingViewSet,
    EntertainmentBuildingViewSet,
    KnowledgeOrInformationBuildingViewSet,
    OtherUtilitarianPublicBuildingViewSet,
    SpecialPurposeSiteViewSet,
    CeremonialSiteViewSet,
    BurialSiteViewSet,
    TradingEmporiaViewSet,
    EnclosureViewSet,
    LengthMeasurementSystemViewSet,
    AreaMeasurementSystemViewSet,
    VolumeMeasurementSystemViewSet,
    WeightMeasurementSystemViewSet,
    TimeMeasurementSystemViewSet,
    GeometricalMeasurementSystemViewSet,
    OtherMeasurementSystemViewSet,
    DebtAndCreditStructureViewSet,
    StoreOfWealthViewSet,
    SourceOfSupportViewSet,
    OccupationalComplexityViewSet,
    SpecialPurposeHouseViewSet,
    OtherSpecialPurposeSiteViewSet,
    LargestCommunicationDistanceViewSet,
    FastestIndividualCommunicationViewSet,
)

# Register views for "sc" app

router.register(
    r"research-assistants", RAViewSet, basename="research-assistant"
)
router.register(
    r"polity-territories", PolityTerritoryViewSet, basename="polity-territory"
)
router.register(
    r"polity-populations",
    PolityPopulationViewSet,
    basename="polity-population",
)
router.register(
    r"population-of-the-largest-settlements",
    PopulationOfTheLargestSettlementViewSet,
    basename="population-of-the-largest-settlement",
)
router.register(
    r"settlement-hierarchies",
    SettlementHierarchyViewSet,
    basename="settlement-hierarchy",
)
router.register(
    r"administrative-levels",
    AdministrativeLevelViewSet,
    basename="administrative-level",
)
router.register(
    r"religious-levels", ReligiousLevelViewSet, basename="religious-level"
)
router.register(
    r"military-levels", MilitaryLevelViewSet, basename="military-level"
)
router.register(
    r"professional-military-officers",
    ProfessionalMilitaryOfficerViewSet,
    basename="professional-military-officer",
)
router.register(
    r"professional-soldiers",
    ProfessionalSoldierViewSet,
    basename="professional-soldier",
)
router.register(
    r"professional-priesthoods",
    ProfessionalPriesthoodViewSet,
    basename="professional-priesthood",
)
router.register(
    r"full-time-bureaucrats",
    FullTimeBureaucratViewSet,
    basename="full-time-bureaucrat",
)
router.register(
    r"examination-systems",
    ExaminationSystemViewSet,
    basename="examination-system",
)
router.register(
    r"merit-promotions", MeritPromotionViewSet, basename="merit-promotion"
)
router.register(
    r"specialized-government-buildings",
    SpecializedGovernmentBuildingViewSet,
    basename="specialized-government-building",
)
router.register(
    r"formal-legal-codes", FormalLegalCodeViewSet, basename="formal-legal-code"
)
router.register(r"judges", JudgeViewSet, basename="judge")
router.register(r"courts", CourtViewSet, basename="court")
router.register(
    r"professional-lawyers",
    ProfessionalLawyerViewSet,
    basename="professional-lawyer",
)
router.register(
    r"irrigation-systems",
    IrrigationSystemViewSet,
    basename="irrigation-system",
)
router.register(
    r"drinking-water-supplies",
    DrinkingWaterSupplySystemViewSet,
    basename="drinking-water-supply-system",
)
router.register(r"markets", MarketViewSet, basename="market")
router.register(
    r"food-storage-sites", FoodStorageSiteViewSet, basename="food-storage-site"
)
router.register(r"roads", RoadViewSet, basename="road")
router.register(r"bridges", BridgeViewSet, basename="bridge")
router.register(r"canals", CanalViewSet, basename="canal")
router.register(r"ports", PortViewSet, basename="port")
router.register(
    r"mines-or-quarries", MinesOrQuarryViewSet, basename="mines-or-quarry"
)
router.register(
    r"mnemonic-devices", MnemonicDeviceViewSet, basename="mnemonic-device"
)
router.register(
    r"nonwritten-records",
    NonwrittenRecordViewSet,
    basename="nonwritten-record",
)
router.register(
    r"written-records", WrittenRecordViewSet, basename="written-record"
)
router.register(r"scripts", ScriptViewSet, basename="script")
router.register(
    r"non-phonetic-writings",
    NonPhoneticWritingViewSet,
    basename="non-phonetic-writing",
)
router.register(
    r"phonetic-alphabetic-writings",
    PhoneticAlphabeticWritingViewSet,
    basename="phonetic-alphabetic-writing",
)
router.register(
    r"lists-tables-and-classifications",
    ListsTablesAndClassificationViewSet,
    basename="lists-tables-and-classifications",
)
router.register(r"calendars", CalendarViewSet, basename="calendar")
router.register(r"sacred-texts", SacredTextViewSet, basename="sacred-text")
router.register(
    r"religious-literatures",
    ReligiousLiteratureViewSet,
    basename="religious-literature",
)
router.register(
    r"practical-literatures",
    PracticalLiteratureViewSet,
    basename="practical-literature",
)
router.register(r"histories", HistoryViewSet, basename="history")
router.register(r"philosophies", PhilosophyViewSet, basename="philosophy")
router.register(
    r"scientific-literatures",
    ScientificLiteratureViewSet,
    basename="scientific-literature",
)
router.register(r"fictions", FictionViewSet, basename="fiction")
router.register(r"articles", ArticleViewSet, basename="article")
router.register(r"tokens", TokenViewSet, basename="token")
router.register(
    r"precious-metals", PreciousMetalViewSet, basename="precious-metal"
)
router.register(r"foreign-coins", ForeignCoinViewSet, basename="foreign-coin")
router.register(
    r"indigenous-coins", IndigenousCoinViewSet, basename="indigenous-coin"
)
router.register(
    r"paper-currencies", PaperCurrencyViewSet, basename="paper-currency"
)
router.register(r"couriers", CourierViewSet, basename="courier")
router.register(
    r"postal-stations", PostalStationViewSet, basename="postal-station"
)
router.register(
    r"general-postal-services",
    GeneralPostalServiceViewSet,
    basename="general-postal-service",
)
router.register(
    r"communal-buildings",
    CommunalBuildingViewSet,
    basename="communal-building",
)
router.register(
    r"utilitarian-public-buildings",
    UtilitarianPublicBuildingViewSet,
    basename="utilitarian-public-building",
)
router.register(
    r"symbolic-buildings",
    SymbolicBuildingViewSet,
    basename="symbolic-building",
)
router.register(
    r"entertainment-buildings",
    EntertainmentBuildingViewSet,
    basename="entertainment-building",
)
router.register(
    r"knowledge-or-information-buildings",
    KnowledgeOrInformationBuildingViewSet,
    basename="knowledge-or-information-building",
)
router.register(
    r"other-utilitarian-public-buildings",
    OtherUtilitarianPublicBuildingViewSet,
    basename="other-utilitarian-public-building",
)
router.register(
    r"special-purpose-sites",
    SpecialPurposeSiteViewSet,
    basename="special-purpose-site",
)
router.register(
    r"ceremonial-sites", CeremonialSiteViewSet, basename="ceremonial-site"
)
router.register(r"burial-sites", BurialSiteViewSet, basename="burial-site")
router.register(
    r"trading-emporia", TradingEmporiaViewSet, basename="trading-emporium"
)
router.register(r"enclosures", EnclosureViewSet, basename="enclosure")
router.register(
    r"length-measurement-systems",
    LengthMeasurementSystemViewSet,
    basename="length-measurement-system",
)
router.register(
    r"area-measurement-systems",
    AreaMeasurementSystemViewSet,
    basename="area-measurement-system",
)
router.register(
    r"volume-measurement-systems",
    VolumeMeasurementSystemViewSet,
    basename="volume-measurement-system",
)
router.register(
    r"weight-measurement-systems",
    WeightMeasurementSystemViewSet,
    basename="weight-measurement-system",
)
router.register(
    r"time-measurement-systems",
    TimeMeasurementSystemViewSet,
    basename="time-measurement-system",
)
router.register(
    r"geometrical-measurement-systems",
    GeometricalMeasurementSystemViewSet,
    basename="geometrical-measurement-system",
)
router.register(
    r"other-measurement-systems",
    OtherMeasurementSystemViewSet,
    basename="other-measurement-system",
)
router.register(
    r"debt-and-credit-structures",
    DebtAndCreditStructureViewSet,
    basename="debt-and-credit-structure",
)
router.register(
    r"stores-of-wealth", StoreOfWealthViewSet, basename="store-of-wealth"
)
router.register(
    r"sources-of-support", SourceOfSupportViewSet, basename="source-of-support"
)
router.register(
    r"occupational-complexities",
    OccupationalComplexityViewSet,
    basename="occupational-complexity",
)
router.register(
    r"special-purpose-houses",
    SpecialPurposeHouseViewSet,
    basename="special-purpose-house",
)
router.register(
    r"other-special-purpose-sites",
    OtherSpecialPurposeSiteViewSet,
    basename="other-special-purpose-site",
)
router.register(
    r"largest-communication-distances",
    LargestCommunicationDistanceViewSet,
    basename="largest-communication-distance",
)
router.register(
    r"fastest-individual-communications",
    FastestIndividualCommunicationViewSet,
    basename="fastest-individual-communication",
)


# Register views for "wf" app

from .views.wf import (
    LongWallViewSet,
    CopperViewSet,
    BronzeViewSet,
    IronViewSet,
    SteelViewSet,
    JavelinViewSet,
    AtlatlViewSet,
    SlingViewSet,
    SelfBowViewSet,
    CompositeBowViewSet,
    CrossbowViewSet,
    TensionSiegeEngineViewSet,
    SlingSiegeEngineViewSet,
    GunpowderSiegeArtilleryViewSet,
    HandheldFirearmViewSet,
    WarClubViewSet,
    BattleAxeViewSet,
    DaggerViewSet,
    SwordViewSet,
    SpearViewSet,
    PolearmViewSet,
    DogViewSet,
    DonkeyViewSet,
    HorseViewSet,
    CamelViewSet,
    ElephantViewSet,
    WoodBarkEtcViewSet,
    LeatherClothViewSet,
    ShieldViewSet,
    HelmetViewSet,
    BreastplateViewSet,
    LimbProtectionViewSet,
    ScaledArmorViewSet,
    LaminarArmorViewSet,
    PlateArmorViewSet,
    SmallVesselsCanoesEtcViewSet,
    MerchantShipPressedIntoServiceViewSet,
    SpecializedMilitaryVesselViewSet,
    SettlementInADefensivePositionViewSet,
    WoodenPalisadeViewSet,
    EarthRampartViewSet,
    DitchViewSet,
    MoatViewSet,
    StoneWallsNonMortaredViewSet,
    StoneWallsMortaredViewSet,
    FortifiedCampViewSet,
    ComplexFortificationViewSet,
    ModernFortificationViewSet,
    ChainmailViewSet,
)

router.register(r"long-walls", LongWallViewSet, basename="long-wall")
router.register(r"coppers", CopperViewSet, basename="copper")
router.register(r"bronzes", BronzeViewSet, basename="bronze")
router.register(r"irons", IronViewSet, basename="iron")
router.register(r"steels", SteelViewSet, basename="steel")
router.register(r"javelins", JavelinViewSet, basename="javelin")
router.register(r"atlatls", AtlatlViewSet, basename="atlatl")
router.register(r"slings", SlingViewSet, basename="sling")
router.register(r"self-bows", SelfBowViewSet, basename="self-bow")
router.register(
    r"composite-bows", CompositeBowViewSet, basename="composite-bow"
)
router.register(r"crossbows", CrossbowViewSet, basename="crossbow")
router.register(
    r"tension-siege-engines",
    TensionSiegeEngineViewSet,
    basename="tension-siege-engine",
)
router.register(
    r"sling-siege-engines",
    SlingSiegeEngineViewSet,
    basename="sling-siege-engine",
)
router.register(
    r"gunpowder-siege-artilleries",
    GunpowderSiegeArtilleryViewSet,
    basename="gunpowder-siege-artillery",
)
router.register(
    r"handheld-firearms", HandheldFirearmViewSet, basename="handheld-firearm"
)
router.register(r"war-clubs", WarClubViewSet, basename="war-club")
router.register(r"battle-axes", BattleAxeViewSet, basename="battle-axe")
router.register(r"daggers", DaggerViewSet, basename="dagger")
router.register(r"swords", SwordViewSet, basename="sword")
router.register(r"spears", SpearViewSet, basename="spear")
router.register(r"polearms", PolearmViewSet, basename="polearm")
router.register(r"dogs", DogViewSet, basename="dog")
router.register(r"donkeys", DonkeyViewSet, basename="donkey")
router.register(r"horses", HorseViewSet, basename="horse")
router.register(r"camels", CamelViewSet, basename="camel")
router.register(r"elephants", ElephantViewSet, basename="elephant")
router.register(r"wood-bark-etc", WoodBarkEtcViewSet, basename="wood-bark-etc")
router.register(r"leathers", LeatherClothViewSet, basename="leather-cloth")
router.register(r"shields", ShieldViewSet, basename="shield")
router.register(r"helmets", HelmetViewSet, basename="helmet")
router.register(r"breastplates", BreastplateViewSet, basename="breastplate")
router.register(
    r"limb-protections", LimbProtectionViewSet, basename="limb-protection"
)
router.register(r"scaled-armors", ScaledArmorViewSet, basename="scaled-armor")
router.register(
    r"laminar-armors", LaminarArmorViewSet, basename="laminar-armor"
)
router.register(r"plate-armors", PlateArmorViewSet, basename="plate-armor")
router.register(
    r"small-vessel-canoe-etc",
    SmallVesselsCanoesEtcViewSet,
    basename="small-vessel-canoe-etc",
)
router.register(
    r"merchant-ship-pressed-into-service",
    MerchantShipPressedIntoServiceViewSet,
    basename="merchant-ship-pressed-into-service",
)
router.register(
    r"specialized-military-vessels",
    SpecializedMilitaryVesselViewSet,
    basename="specialized-military-vessel",
)
router.register(
    r"settlement-in-defensive-positions",
    SettlementInADefensivePositionViewSet,
    basename="settlement-in-defensive-position",
)
router.register(
    r"wooden-palisades", WoodenPalisadeViewSet, basename="wooden-palisade"
)
router.register(
    r"earth-ramparts", EarthRampartViewSet, basename="earth-rampart"
)
router.register(r"ditches", DitchViewSet, basename="ditch")
router.register(r"moats", MoatViewSet, basename="moat")
router.register(
    r"stone-walls-non-mortared",
    StoneWallsNonMortaredViewSet,
    basename="stone-walls-non-mortared",
)
router.register(
    r"stone-walls-mortared",
    StoneWallsMortaredViewSet,
    basename="stone-walls-mortared",
)
router.register(
    r"fortified-camps", FortifiedCampViewSet, basename="fortified-camp"
)
router.register(
    r"complex-fortifications",
    ComplexFortificationViewSet,
    basename="complex-fortification",
)
router.register(
    r"modern-fortifications",
    ModernFortificationViewSet,
    basename="modern-fortification",
)
router.register(r"chainmails", ChainmailViewSet, basename="chainmail")


# Register all the views with the router

urlpatterns = [
    path("", include(router.urls)),
    path(
        "api-auth/", include("rest_framework.urls", namespace="rest_framework")
    ),
]
