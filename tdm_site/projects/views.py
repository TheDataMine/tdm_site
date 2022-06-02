from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, ListView, FormView
from rest_framework.views import APIView
from django.shortcuts import render
from django.core.paginator import Paginator

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


class ProjectSearchView(FormView):
    form_class = SearchProjectsForm
    template_name = "projects/project_search.html"

project_search_view = ProjectSearchView.as_view()

def project_search_result_view(request):
    queryset = Project.objects.all()
    year = request.GET.get('year')
    domain = request.GET.get('domain')
    citizenship_status = request.GET.get('citizenship_status')

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

