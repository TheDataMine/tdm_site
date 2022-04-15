from django.urls import path

from tdm_site.companies.views import (
    company_detail_view,
    company_list_view,
)

app_name = "companies"
urlpatterns = [
    path("", view=company_list_view, name="list"),
    path("<str:slug>/", view=company_detail_view, name="detail"),
]
