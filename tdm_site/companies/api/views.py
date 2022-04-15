from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from tdm_site.companies.models import Company

from .serializers import CompanySerializer


class CompanyViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    lookup_field = "name"
