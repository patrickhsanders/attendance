from django.contrib import admin
from .models import Project
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','course','nextProject',)
    list_filter = ('course',)
    search_fields = ('description',)

admin.site.register(Project, ProjectAdmin)
