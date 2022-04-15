from django.contrib import admin
from .models import Project, CitizenshipStatus

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at", "updated_at",)

class CitizenshipStatusAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("status",)}
    list_display = ('status', 'description')

admin.site.register(Project, ProjectAdmin)
admin.site.register(CitizenshipStatus, CitizenshipStatusAdmin)
