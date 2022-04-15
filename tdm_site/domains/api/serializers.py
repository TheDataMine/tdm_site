from rest_framework import serializers
from tdm_site.companies.models import Domain


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ["domain",]

        extra_kwargs = {
            "url": {"view_name": "api:domain-detail", "lookup_field": "domain"}
        }
