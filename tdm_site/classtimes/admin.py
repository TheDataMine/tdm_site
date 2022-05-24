from django.contrib import admin
from .models import Labtime, Lecturetime

class LabtimeAdmin(admin.ModelAdmin):
    pass

class LecturetimeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Labtime, LabtimeAdmin)
admin.site.register(Lecturetime, LecturetimeAdmin)