from django.contrib import admin
from .models import Project, StudentProject
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','course','weight')
    list_filter = ('course',)
    list_editable = ('weight',)
    ordering = ('weight',)
    # search_fields = ('description',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(StudentProject)