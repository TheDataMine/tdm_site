from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import generics
from tdm_site.projects.models import Project

from .serializers import ProjectSerializer


class ProjectViewSet(ListModelMixin, GenericViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get_queryset(self):
        """
        Optionally restricts the returned projects by filtering against
        a variety of form fields.
        """
        queryset = Project.objects.all()
        year = self.request.query_params.get('year')
        domain = self.request.query_params.get('domain')
        citizenship_status = self.request.query_params.get('citizenship_status')

        keywords = self.request.query_params.get('keywords')
        tools = self.request.query_params.get('tools')
        labtimes = self.request.query_params.get('labtimes')
        lecturetimes = self.request.query_params.get('lecturetimes')

        if year is not None:
            queryset = queryset.filter(year=year)

        if domain is not None:
            queryset = queryset.filter(domain=domain)

        if citizenship_status is not None:
            queryset = queryset.filter(citizenship_status=citizenship_status)

        if keywords is not None:
            queryset = queryset.filter(keywords__in=keywords)

        if tools is not None:
            queryset = queryset.filter(tools__in=tools)

        if labtimes is not None:
            queryset = queryset.filter(labtimes__in=labtimes)

        if lecturetimes is not None:
            queryset = queryset.filter(lecturetimes__in=lecturetimes)

        return queryset
