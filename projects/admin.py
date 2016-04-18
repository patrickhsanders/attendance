from django.contrib import admin
from .models import Project, StudentProject
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','course','weight')
    list_filter = ('course',)
    list_editable = ('weight',)
    ordering = ('weight',)
    # search_fields = ('description',)

class StudentProjectAdmin(admin.ModelAdmin):
    list_display = ('student', 'project', 'grade', 'derived_days', 'derived_hours')
    list_filter = ('grade', 'project', 'student')
    list_filter = ('student', 'project', 'grade', 'derived_days', 'derived_hours')

admin.site.register(Project, ProjectAdmin)
admin.site.register(StudentProject, StudentProjectAdmin)