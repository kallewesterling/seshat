from rest_framework import viewsets

from ._mixins import (
    MixinSeshatAPIAuth,
    MixinSeshatAPISerializer,
    SeshatAPIPagination,
)

from ...rt.models import (
    Widespread_religion,
    Official_religion,
    Elites_religion,
    Theo_sync_dif_rel,
    Sync_rel_pra_ind_beli,
    Religious_fragmentation,
    Gov_vio_freq_rel_grp,
    Gov_res_pub_wor,
    Gov_res_pub_pros,
    Gov_res_conv,
    Gov_press_conv,
    Gov_res_prop_own_for_rel_grp,
    Tax_rel_adh_act_ins,
    Gov_obl_rel_grp_ofc_reco,
    Gov_res_cons_rel_buil,
    Gov_res_rel_edu,
    Gov_res_cir_rel_lit,
    Gov_dis_rel_grp_occ_fun,
    Soc_vio_freq_rel_grp,
    Soc_dis_rel_grp_occ_fun,
    Gov_press_conv_for_aga,
)


class WidespreadReligionViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Widespread Religions.
    """
    model = Widespread_religion
    pagination_class = SeshatAPIPagination


class OfficialReligionViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Official Religions.
    """
    model = Official_religion
    pagination_class = SeshatAPIPagination


class ElitesReligionViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Elites Religions.
    """
    model = Elites_religion
    pagination_class = SeshatAPIPagination


class TheoSyncDifRelViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Theo Sync Dif Rels.
    """
    model = Theo_sync_dif_rel
    pagination_class = SeshatAPIPagination


class SyncRelPraIndBeliViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Sync Rel Pra Ind Belis.
    """
    model = Sync_rel_pra_ind_beli
    pagination_class = SeshatAPIPagination


class ReligiousFragmentationViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Religious Fragmentations.
    """
    model = Religious_fragmentation
    pagination_class = SeshatAPIPagination


class GovVioFreqRelGrpViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Gov Vio Freq Rel Grps.
    """
    model = Gov_vio_freq_rel_grp
    pagination_class = SeshatAPIPagination


class GovResPubWorViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Gov Res Pub Wors.
    """
    model = Gov_res_pub_wor
    pagination_class = SeshatAPIPagination


class GovResPubProsViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Gov Res Pub Proses.
    """
    model = Gov_res_pub_pros
    pagination_class = SeshatAPIPagination


class GovResConvViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Gov Res Convs.
    """
    model = Gov_res_conv
    pagination_class = SeshatAPIPagination


class GovPressConvViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Gov Press Convs.
    """
    model = Gov_press_conv
    pagination_class = SeshatAPIPagination


class GovResPropOwnForRelGrpViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Gov Res Prop Own For Rel Grps.
    """
    model = Gov_res_prop_own_for_rel_grp
    pagination_class = SeshatAPIPagination


class TaxRelAdhActInsViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Tax Rel Adh Act Inses.
    """
    model = Tax_rel_adh_act_ins
    pagination_class = SeshatAPIPagination


class GovOblRelGrpOfcRecoViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Gov Obl Rel Grp Ofc Recos.
    """
    model = Gov_obl_rel_grp_ofc_reco
    pagination_class = SeshatAPIPagination


class GovResConsRelBuilViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Gov Res Cons Rel Buils.
    """
    model = Gov_res_cons_rel_buil
    pagination_class = SeshatAPIPagination


class GovResRelEduViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Gov Res Rel Edus.
    """
    model = Gov_res_rel_edu
    pagination_class = SeshatAPIPagination


class GovResCirRelLitViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Gov Res Cir Rel Lits.
    """
    model = Gov_res_cir_rel_lit
    pagination_class = SeshatAPIPagination


class GovDisRelGrpOccFunViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Gov Dis Rel Grp Occ Funs.
    """
    model = Gov_dis_rel_grp_occ_fun
    pagination_class = SeshatAPIPagination


class SocVioFreqRelGrpViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Soc Vio Freq Rel Grps.
    """
    model = Soc_vio_freq_rel_grp
    pagination_class = SeshatAPIPagination


class SocDisRelGrpOccFunViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Soc Dis Rel Grp Occ Funs.
    """
    model = Soc_dis_rel_grp_occ_fun
    pagination_class = SeshatAPIPagination


class GovPressConvForAgaViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Gov Press Conv For Agas.
    """
    model = Gov_press_conv_for_aga
    pagination_class = SeshatAPIPagination
