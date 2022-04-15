from django.contrib import admin
from .models import Tool

class ToolAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Tool, ToolAdmin)
