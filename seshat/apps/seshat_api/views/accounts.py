from rest_framework import viewsets

from ...accounts.models import Profile, Seshat_Expert, Seshat_Task

from ._mixins import (
    MixinSeshatAPIAuth,
    MixinSeshatAPISerializer,
)
from ._permissions import ONLY_ADMIN_PERMISSIONS


class ProfileViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ReadOnlyModelViewSet
):
    """
    A viewset for viewing user profiles.
    """

    model = Profile
    lookup_field = "user__username"
    permissions_dict = ONLY_ADMIN_PERMISSIONS


class SeshatExpertViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ModelViewSet
):
    """
    A viewset for viewing and editing Seshat Experts.
    """

    model = Seshat_Expert
    lookup_field = "user__username"
    permissions_dict = ONLY_ADMIN_PERMISSIONS


class SeshatTaskViewSet(
    MixinSeshatAPISerializer, MixinSeshatAPIAuth, viewsets.ReadOnlyModelViewSet
):
    """
    A viewset for viewing Seshat Tasks.
    """

    model = Seshat_Task
    permissions_dict = ONLY_ADMIN_PERMISSIONS
    fields = "__all__"
