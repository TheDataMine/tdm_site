from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, ListView

from tdm_site.tools.models import Tool


class ToolDetailView(DetailView):

    model = Tool
    slug_field = "slug"
    slug_url_kwarg = "slug"


tool_detail_view = ToolDetailView.as_view()


class ToolListView(ListView):
    
    model = Tool
    paginate_by = 25


tool_list_view = ToolListView.as_view()
