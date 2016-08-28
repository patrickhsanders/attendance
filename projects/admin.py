from django.contrib import admin
from .models import Project, StudentProject
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'estimated_completion_days', 'weight')
    list_filter = ('course',)
    list_editable = ('weight', 'estimated_completion_days')
    ordering = ('weight',)


class StudentProjectAdmin(admin.ModelAdmin):
    list_display = ('student', 'project', 'derived_days', 'derived_hours')
    list_filter = ('project', 'student')


admin.site.register(Project, ProjectAdmin)
admin.site.register(StudentProject, StudentProjectAdmin)
