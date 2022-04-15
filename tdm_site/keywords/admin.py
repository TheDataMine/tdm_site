from django.contrib import admin
from .models import Keyword

class KeywordAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("keyword",)}

admin.site.register(Keyword, KeywordAdmin)
