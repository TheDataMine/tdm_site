from rest_framework import serializers
from tdm_site.projects.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["year", "title", "domain", "keywords", "tools", "citizenship_status", "classtimes", "summary", "description",]

        extra_kwargs = {
            "url": {"view_name": "api:project-detail", "lookup_field": "title"}
        }
