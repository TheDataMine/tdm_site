from django.urls import path

from tdm_site.keywords.views import (
    keyword_detail_view,
    keyword_list_view,
)

app_name = "keywords"
urlpatterns = [
    path("", view=keyword_list_view, name="list"),
    path("<str:slug>/", view=keyword_detail_view, name="detail"),
]
