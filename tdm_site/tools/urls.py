from django.urls import path

from tdm_site.tools.views import (
    tool_detail_view,
    tool_list_view,
)

app_name = "tool"
urlpatterns = [
    path("", view=tool_list_view, name="list"),
    path("<str:slug>/", view=tool_detail_view, name="detail"),
]
