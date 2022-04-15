from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, ListView

from tdm_site.companies.models import Company


class CompanyDetailView(DetailView):

    model = Company
    slug_field = "slug"
    slug_url_kwarg = "slug"


company_detail_view = CompanyDetailView.as_view()


class CompanyListView(ListView):
    
    model = Company
    paginate_by = 25


company_list_view = CompanyListView.as_view()
