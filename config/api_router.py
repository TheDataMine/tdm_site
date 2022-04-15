from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from tdm_site.users.api.views import UserViewSet
from tdm_site.companies.api.views import CompanyViewSet
from tdm_site.projects.api.views import ProjectViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("companies", CompanyViewSet)
router.register("projects", ProjectViewSet)


app_name = "api"
urlpatterns = router.urls
