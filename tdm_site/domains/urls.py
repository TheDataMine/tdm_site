from django.urls import path

from tdm_site.domains.views import (
    domain_detail_view,
    domain_list_view,
)

app_name = "domains"
urlpatterns = [
    path("", view=domain_list_view, name="list"),
    path("<str:slug>/", view=domain_detail_view, name="detail"),
]
