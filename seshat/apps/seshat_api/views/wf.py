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


from ...wf.models import (
    Long_wall,
    Copper,
    Bronze,
    Iron,
    Steel,
    Javelin,
    Atlatl,
    Sling,
    Self_bow,
    Composite_bow,
    Crossbow,
    Tension_siege_engine,
    Sling_siege_engine,
    Gunpowder_siege_artillery,
    Handheld_firearm,
    War_club,
    Battle_axe,
    Dagger,
    Sword,
    Spear,
    Polearm,
    Dog,
    Donkey,
    Horse,
    Camel,
    Elephant,
    Wood_bark_etc,
    Leather_cloth,
    Shield,
    Helmet,
    Breastplate,
    Limb_protection,
    Scaled_armor,
    Laminar_armor,
    Plate_armor,
    Small_vessels_canoes_etc,
    Merchant_ships_pressed_into_service,
    Specialized_military_vessel,
    Settlements_in_a_defensive_position,
    Wooden_palisade,
    Earth_rampart,
    Ditch,
    Moat,
    Stone_walls_non_mortared,
    Stone_walls_mortared,
    Fortified_camp,
    Complex_fortification,
    Modern_fortification,
    Chainmail,
)


class LongWallViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Long Walls.
    """
    model = Long_wall
    pagination_class = SeshatAPIPagination


class CopperViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Coppers.
    """
    model = Copper
    pagination_class = SeshatAPIPagination


class BronzeViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Bronzes.
    """
    model = Bronze
    pagination_class = SeshatAPIPagination


class IronViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Irons.
    """
    model = Iron
    pagination_class = SeshatAPIPagination


class SteelViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Steels.
    """
    model = Steel
    pagination_class = SeshatAPIPagination


class JavelinViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Javelins.
    """
    model = Javelin
    pagination_class = SeshatAPIPagination


class AtlatlViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Atlatls.
    """
    model = Atlatl
    pagination_class = SeshatAPIPagination


class SlingViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Slings.
    """
    model = Sling
    pagination_class = SeshatAPIPagination


class SelfBowViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Self Bows.
    """
    model = Self_bow
    pagination_class = SeshatAPIPagination


class CompositeBowViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Composite Bows.
    """
    model = Composite_bow
    pagination_class = SeshatAPIPagination


class CrossbowViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Crossbows.
    """
    model = Crossbow
    pagination_class = SeshatAPIPagination


class TensionSiegeEngineViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Tension Siege Engines.
    """
    model = Tension_siege_engine
    pagination_class = SeshatAPIPagination


class SlingSiegeEngineViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Sling Siege Engines.
    """
    model = Sling_siege_engine
    pagination_class = SeshatAPIPagination


class GunpowderSiegeArtilleryViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Gunpowder Siege Artilleries.
    """
    model = Gunpowder_siege_artillery
    pagination_class = SeshatAPIPagination


class HandheldFirearmViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Handheld Firearms.
    """
    model = Handheld_firearm
    pagination_class = SeshatAPIPagination


class WarClubViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing War Clubs.
    """
    model = War_club
    pagination_class = SeshatAPIPagination


class BattleAxeViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Battle Axes.
    """
    model = Battle_axe
    pagination_class = SeshatAPIPagination


class DaggerViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Daggers.
    """
    model = Dagger
    pagination_class = SeshatAPIPagination


class SwordViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Swords.
    """
    model = Sword
    pagination_class = SeshatAPIPagination


class SpearViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Spears.
    """
    model = Spear
    pagination_class = SeshatAPIPagination


class PolearmViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Polearms.
    """
    model = Polearm
    pagination_class = SeshatAPIPagination


class DogViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Dogs.
    """
    model = Dog
    pagination_class = SeshatAPIPagination


class DonkeyViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Donkeys.
    """
    model = Donkey
    pagination_class = SeshatAPIPagination


class HorseViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Horses.
    """
    model = Horse
    pagination_class = SeshatAPIPagination


class CamelViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Camels.
    """
    model = Camel
    pagination_class = SeshatAPIPagination


class ElephantViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Elephants.
    """
    model = Elephant
    pagination_class = SeshatAPIPagination


class WoodBarkEtcViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Wood bark, etc.
    """
    model = Wood_bark_etc
    pagination_class = SeshatAPIPagination


class LeatherClothViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Leather Cloth.
    """
    model = Leather_cloth
    pagination_class = SeshatAPIPagination


class ShieldViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Shields.
    """
    model = Shield
    pagination_class = SeshatAPIPagination


class HelmetViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Helmets.
    """
    model = Helmet
    pagination_class = SeshatAPIPagination


class BreastplateViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Breastplates.
    """
    model = Breastplate
    pagination_class = SeshatAPIPagination


class LimbProtectionViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Limb Protections.
    """
    model = Limb_protection
    pagination_class = SeshatAPIPagination


class ScaledArmorViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Scaled Armors.
    """
    model = Scaled_armor
    pagination_class = SeshatAPIPagination


class LaminarArmorViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Laminar Armors.
    """
    model = Laminar_armor
    pagination_class = SeshatAPIPagination


class PlateArmorViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Plate Armors.
    """
    model = Plate_armor
    pagination_class = SeshatAPIPagination


class SmallVesselsCanoesEtcViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Small Vessels, Canoes, etc.
    """
    model = Small_vessels_canoes_etc
    pagination_class = SeshatAPIPagination


class MerchantShipPressedIntoServiceViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Merchant Ships Pressed Into Services.
    """
    model = Merchant_ships_pressed_into_service
    pagination_class = SeshatAPIPagination


class SpecializedMilitaryVesselViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Specialized Military Vessels.
    """
    model = Specialized_military_vessel
    pagination_class = SeshatAPIPagination


class SettlementInADefensivePositionViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Settlements in a Defensive Position.
    """
    model = Settlements_in_a_defensive_position
    pagination_class = SeshatAPIPagination


class WoodenPalisadeViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Wooden Palisades.
    """
    model = Wooden_palisade
    pagination_class = SeshatAPIPagination


class EarthRampartViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Earth Ramparts.
    """
    model = Earth_rampart
    pagination_class = SeshatAPIPagination


class DitchViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Ditches.
    """
    model = Ditch
    pagination_class = SeshatAPIPagination


class MoatViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Moats.
    """
    model = Moat
    pagination_class = SeshatAPIPagination


class StoneWallsNonMortaredViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Stone Walls Non Mortared.
    """
    model = Stone_walls_non_mortared
    pagination_class = SeshatAPIPagination


class StoneWallsMortaredViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Stone Walls Mortared.
    """
    model = Stone_walls_mortared
    pagination_class = SeshatAPIPagination


class FortifiedCampViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Fortified Camps.
    """
    model = Fortified_camp
    pagination_class = SeshatAPIPagination


class ComplexFortificationViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Complex Fortifications.
    """
    model = Complex_fortification
    pagination_class = SeshatAPIPagination


class ModernFortificationViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Modern Fortifications.
    """
    model = Modern_fortification
    pagination_class = SeshatAPIPagination


class ChainmailViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Chainmails.
    """
    model = Chainmail
    pagination_class = SeshatAPIPagination
