from django.contrib import admin
from .models import Register,DailyAttendance, DailyStatistics

# Register your models here.

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('student','checkin','checkout','forgot_to_checkout')
    list_filter = ('student', 'checkin','checkout','forgot_to_checkout')

class DailyStatisticsAdmin(admin.ModelAdmin):
    list_display = ('date', 'average_checkin', 'average_hours_spent', 'percent_students_present')

admin.site.register(Register,RegisterAdmin)
admin.site.register(DailyAttendance)
admin.site.register(DailyStatistics,DailyStatisticsAdmin)