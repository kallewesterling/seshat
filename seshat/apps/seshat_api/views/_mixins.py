from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny

from ..serializers import GeneralSerializer
from rest_framework.serializers import HyperlinkedRelatedField

STANDARD_API_AUTHENTICATION = {
    "HEAD": [AllowAny],
    "OPTIONS": [AllowAny],
    "GET": [AllowAny],
    "POST": [IsAuthenticated],
    "PUT": [IsAuthenticated],
    "PATCH": [IsAuthenticated],
    "DELETE": [IsAuthenticated],
}
"""Defines the standard authentication for the API, if no other is specified in the view."""


class SeshatAPIPagination(PageNumberPagination):
    """
    Custom pagination class for the API.
    """
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class MixinSeshatAPIAuth:
    """
    Mixin class to set the authentication classes for the API.
    """
    def get_permissions(self):
        try:
            permissions_dict = self.permissions_dict
        except AttributeError:
            permissions_dict = STANDARD_API_AUTHENTICATION

        return [
            permission()
            for permission in permissions_dict[self.request.method]
        ]

class MixinSeshatAPISerializer:
    def get_serializer_class(self):
        # Set model to self.model
        GeneralSerializer.Meta.model = self.model

        # Set fields to self.fields
        try:
            GeneralSerializer.Meta.fields = self.fields
        except AttributeError:
            GeneralSerializer.Meta.fields = "__all__"

        return GeneralSerializer

    def get_queryset(self):
        return self.model.objects.all()
