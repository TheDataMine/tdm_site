from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, ListView

from tdm_site.companies.models import Company

from tdm_site.projects.models import Project


class CompanyDetailView(DetailView):

    model = Company
    slug_field = "slug"
    slug_url_kwarg = "slug"
    
    def get_object(self):
        """
        Return the list of items for this view.
        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        company = super(CompanyDetailView, self).get_object()
        
        # Get projects for this company
        projects = Project.objects.filter(company__name=company.name)
        
        if yr := self.request.GET.get('year'):
            projects = projects.filter(year=yr)
            
        return projects


company_detail_view = CompanyDetailView.as_view()


class CompanyListView(ListView):
    
    model = Company


company_list_view = CompanyListView.as_view()
