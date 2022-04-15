from rest_framework import serializers
from tdm_site.companies.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["name",]

        extra_kwargs = {
            "url": {"view_name": "api:company-detail", "lookup_field": "name"}
        }
