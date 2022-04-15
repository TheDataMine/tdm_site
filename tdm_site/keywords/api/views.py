from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from tdm_site.companies.models import Keyword

from .serializers import KeywordSerializer


class KeywordViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = KeywordSerializer
    queryset = Keyword.objects.all()
    lookup_field = "keyword"
