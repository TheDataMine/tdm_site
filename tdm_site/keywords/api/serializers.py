from rest_framework import serializers
from tdm_site.companies.models import Keyword


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ["keyword",]

        extra_kwargs = {
            "url": {"view_name": "api:keyword-detail", "lookup_field": "keyword"}
        }
