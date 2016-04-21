from django.contrib import admin
from .models import Register,DailyAttendance

# Register your models here.

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('student','checkin','checkout','forgot_to_checkout')
    list_filter = ('student', 'checkin','checkout','forgot_to_checkout')

admin.site.register(Register,RegisterAdmin)
admin.site.register(DailyAttendance)
