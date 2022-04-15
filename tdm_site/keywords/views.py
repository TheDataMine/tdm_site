from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, ListView

from tdm_site.keywords.models import Keyword


class KeywordDetailView(DetailView):

    model = Keyword
    slug_field = "slug"
    slug_url_kwarg = "slug"


keyword_detail_view = KeywordDetailView.as_view()


class KeywordListView(ListView):
    
    model = Keyword
    paginate_by = 25


keyword_list_view = KeywordListView.as_view()
