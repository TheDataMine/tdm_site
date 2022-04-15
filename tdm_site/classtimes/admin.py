from django.contrib import admin
from .models import Classtime

class ClasstimeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Classtime, ClasstimeAdmin)
