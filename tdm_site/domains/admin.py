from django.contrib import admin
from .models import Domain

class DomainAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("domain",)}

admin.site.register(Domain, DomainAdmin)
