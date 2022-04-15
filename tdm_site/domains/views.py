from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, ListView

from tdm_site.domains.models import Domain


class DomainDetailView(DetailView):

    model = Domain
    slug_field = "slug"
    slug_url_kwarg = "slug"


domain_detail_view = DomainDetailView.as_view()


class DomainListView(ListView):
    
    model = Domain
    paginate_by = 25


domain_list_view = DomainListView.as_view()
