from django.contrib import admin
from .models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email','start_date','course', 'current_project', 'active',)
    list_filter = ('course', 'active','current_project',)
    search_fields = ('first_name', 'last_name', 'email',)

admin.site.register(Student, StudentAdmin)
