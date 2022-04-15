from rest_framework import serializers
from tdm_site.companies.models import Tool


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ["tool",]

        extra_kwargs = {
                "url": {"view_name": "api:tool-detail", "lookup_field": "name"}
        }
