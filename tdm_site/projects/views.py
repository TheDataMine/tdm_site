from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, ListView, FormView
from rest_framework.views import APIView
from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.exceptions import ImproperlyConfigured
from django.db.models import Count

from tdm_site.projects.models import Project

from .forms import SearchProjectsForm
from .models import Project


class ProjectDetailView(DetailView):

    model = Project
    slug_field = "slug"
    slug_url_kwarg = "slug"


project_detail_view = ProjectDetailView.as_view()


class ProjectListView(ListView):
    
    model = Project
    paginate_by = 10

project_list_view = ProjectListView.as_view()


class ProjectListByYearView(ListView):
    
    model = Project
    template_name = "projects/project_list_by_year.html"
    
    def get_queryset(self):
        """
        Return the list of items for this view.
        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        qs = super(ProjectListByYearView, self).get_queryset()
        return qs.order_by('-year', 'company__name').distinct('year', 'company__name')

project_list_by_year_view = ProjectListByYearView.as_view()


class ProjectSearchView(FormView):
    form_class = SearchProjectsForm
    template_name = "projects/project_search.html"

project_search_view = ProjectSearchView.as_view()

def project_search_result_view(request):
    queryset = Project.objects.all()
    year = request.GET.get('year')
    domain = request.GET.get('domain')
    citizenship_status = request.GET.get('citizenship_status')
    registration_status = request.GET.get('registration_status')
    deafpods_bool = request.GET.get('deafpods_bool')
    ndmn_bool = request.GET.get('ndmn_bool')
    indy_bool = request.GET.get('indy_bool')
    online_bool = request.GET.get('online_bool')
    rockies_bool = request.GET.get('rockies_bool')
    #wl_bool = request.GET.get('wl_bool')

    keywords = request.GET.getlist('keywords')
    tools = request.GET.getlist('tools')
    lab_times = request.GET.getlist('lab_times')
    lecture_times = request.GET.getlist('lecture_times')

    if year not in ['', None]:
        queryset = queryset.filter(year=year)

    if domain not in ['', None]:
        queryset = queryset.filter(domain=domain)

    if citizenship_status not in ['', None]:
        queryset = queryset.filter(citizenship_status=citizenship_status)

    if registration_status not in ['', None]:
        queryset = queryset.filter(registration_status=registration_status)

    if deafpods_bool not in ['', None]:
        queryset = queryset.filter(deafpods_bool=deafpods_bool)

    if indy_bool not in ['', None]:
        queryset = queryset.filter(indy_bool=indy_bool)

    if rockies_bool not in ['', None]:
        queryset = queryset.filter(rockies_bool=rockies_bool)

    #if wl_bool not in ['', None]:
    #    queryset = queryset.filter(wl_bool=wl_bool)

    if ndmn_bool not in ['', None]:
        queryset = queryset.filter(ndmn_bool=ndmn_bool)

    if online_bool not in ['', None]:
        queryset = queryset.filter(online_bool=online_bool)

    if keywords:
        queryset = queryset.filter(keywords__in=keywords)

    if tools:
        queryset = queryset.filter(tools__in=tools)

    if lab_times:
        queryset = queryset.filter(labtimes__in=lab_times)

    if lecture_times:
        queryset = queryset.filter(lecturetimes__in=lecture_times)

    paginator = Paginator(queryset, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'projects/project_list.html', context={'page_obj': page_obj})

