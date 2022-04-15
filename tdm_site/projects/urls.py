from django.urls import path

from tdm_site.projects.views import (
    project_detail_view,
    project_list_view,
    project_search_view,
    project_search_result_view,
)

app_name = "projects"
urlpatterns = [
    path("", view=project_list_view, name="list"),
    path("search", view=project_search_view, name="search"),
    path("search/query/", view=project_search_result_view, name="search_results"),
    path("<str:slug>/", view=project_detail_view, name="detail"),
]
