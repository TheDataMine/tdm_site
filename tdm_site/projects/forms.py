from django import forms

from .models import CitizenshipStatus, Project

from tdm_site.domains.models import Domain
from tdm_site.keywords.models import Keyword
from tdm_site.tools.models import Tool
from tdm_site.classtimes.models import Classtime

def get_choices():
    return list(zip(list(Project.objects.order_by().values_list("year", flat=True).distinct()), [int(v) for v in Project.objects.order_by().values_list("year", flat=True).distinct()]))

class SearchProjectsForm(forms.Form):
    year = forms.ChoiceField(choices=get_choices, required=False, widget=forms.Select(attrs={"class": "form-control"}))
    domain = forms.ModelChoiceField(queryset=Domain.objects.all(), required=False, widget=forms.Select(attrs={"class": "form-control"}))
    keywords = forms.ModelMultipleChoiceField(queryset=Keyword.objects.all(), required=False, widget=forms.SelectMultiple(attrs={"class": "form-control"}))
    tools = forms.ModelMultipleChoiceField(queryset=Tool.objects.all(), required=False, widget=forms.SelectMultiple(attrs={"class": "form-control"}))
    citizenship_status = forms.ModelChoiceField(queryset=CitizenshipStatus.objects.all(), required=False, widget=forms.Select(attrs={"class": "form-control"}))
    class_times = forms.ModelMultipleChoiceField(queryset=Classtime.objects.all(), required=False, widget=forms.SelectMultiple(attrs={"class": "form-control"}))

