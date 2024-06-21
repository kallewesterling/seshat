from rest_framework import viewsets

from ._mixins import (
    MixinSeshatAPIAuth,
    MixinSeshatAPISerializer,
    SeshatAPIPagination,
)

from ...general.models import (
    Polity_research_assistant,
    Polity_original_name,
    Polity_alternative_name,
    Polity_duration,
    Polity_peak_years,
    Polity_degree_of_centralization,
    Polity_suprapolity_relations,
    Polity_utm_zone,
    Polity_capital,
    Polity_language,
    Polity_linguistic_family,
    Polity_language_genus,
    Polity_religion_genus,
    Polity_religion_family,
    Polity_religion,
    Polity_relationship_to_preceding_entity,
    Polity_preceding_entity,
    Polity_succeeding_entity,
    Polity_supracultural_entity,
    Polity_scale_of_supracultural_interaction,
    Polity_alternate_religion_genus,
    Polity_alternate_religion_family,
    Polity_alternate_religion,
    Polity_expert,
    Polity_editor,
    Polity_religious_tradition,
)


class PolityResearchAssistantViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Polity Research Assistants.
    """
    model = Polity_research_assistant
    pagination_class = SeshatAPIPagination


class PolityOriginalNameViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Polity Original Names.
    """
    model = Polity_original_name
    pagination_class = SeshatAPIPagination


class PolityAlternativeNameViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Polity Alternative Names.
    """
    model = Polity_alternative_name
    pagination_class = SeshatAPIPagination


class PolityDurationViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Polity Durations.
    """
    model = Polity_duration
    pagination_class = SeshatAPIPagination


class PolityPeakYearsViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Polity Peak Years.
    """
    model = Polity_peak_years
    pagination_class = SeshatAPIPagination


class PolityDegreeOfCentralizationViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Polity Degrees of Centralization.
    """
    model = Polity_degree_of_centralization
    pagination_class = SeshatAPIPagination


class PolitySuprapolityRelationsViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Polity Suprapolity Relations.
    """
    model = Polity_suprapolity_relations
    pagination_class = SeshatAPIPagination


class PolityUTMZoneViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Polity UTM Zones.
    """
    model = Polity_utm_zone
    pagination_class = SeshatAPIPagination


class PolityCapitalViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Polity Capitals.
    """
    model = Polity_capital
    pagination_class = SeshatAPIPagination


class PolityLanguageViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Polity Languages.
    """
    model = Polity_language
    pagination_class = SeshatAPIPagination


class PolityLinguisticFamilyViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Polity Linguistic Families.
    """
    model = Polity_linguistic_family
    pagination_class = SeshatAPIPagination


class PolityLanguageGenusViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Polity Language Genuses.
    """
    model = Polity_language_genus
    pagination_class = SeshatAPIPagination


class PolityReligionGenusViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Polity Religion Genuses.
    """
    model = Polity_religion_genus
    pagination_class = SeshatAPIPagination


class PolityReligionFamilyViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Polity Religion Families.
    """
    model = Polity_religion_family
    pagination_class = SeshatAPIPagination


class PolityReligionViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Polity Religions.
    """
    model = Polity_religion
    pagination_class = SeshatAPIPagination


class PolityRelationshipToPrecedingEntityViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Polity Relationships to Preceding Entities.
    """
    model = Polity_relationship_to_preceding_entity
    pagination_class = SeshatAPIPagination


class PolityPrecedingEntityViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Polity Preceding Entities.
    """
    model = Polity_preceding_entity
    pagination_class = SeshatAPIPagination


class PolitySucceedingEntityViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Polity Succeeding Entities.
    """
    model = Polity_succeeding_entity
    pagination_class = SeshatAPIPagination


class PolitySupraculturalEntityViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Polity Supracultural Entities.
    """
    model = Polity_supracultural_entity
    pagination_class = SeshatAPIPagination


class PolityScaleOfSupraculturalInteractionViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Polity Scales of Supracultural Interaction.
    """
    model = Polity_scale_of_supracultural_interaction
    pagination_class = SeshatAPIPagination


class PolityAlternateReligionGenusViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Polity Alternate Religion Genuses.
    """
    model = Polity_alternate_religion_genus
    pagination_class = SeshatAPIPagination


class PolityAlternateReligionFamilyViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Polity Alternate Religion Families.
    """
    model = Polity_alternate_religion_family
    pagination_class = SeshatAPIPagination


class PolityAlternateReligionViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Polity Alternate Religions.
    """
    model = Polity_alternate_religion
    pagination_class = SeshatAPIPagination


class PolityExpertViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Polity Experts.
    """
    model = Polity_expert
    pagination_class = SeshatAPIPagination


class PolityEditorViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Polity Editors.
    """
    model = Polity_editor
    pagination_class = SeshatAPIPagination


class PolityReligiousTraditionViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Polity Religious Traditions.
    """
    model = Polity_religious_tradition
    pagination_class = SeshatAPIPagination
