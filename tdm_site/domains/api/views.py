from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from tdm_site.companies.models import Domain

from .serializers import DomainSerializer


class DomainViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = DomainSerializer
    queryset = Domain.objects.all()
    lookup_field = "domain"
