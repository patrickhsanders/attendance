from django.contrib import admin
from .models import Register

# Register your models here.

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('student','checkin','checkout')
    list_filter = ('student', 'checkin','checkout')

admin.site.register(Register,RegisterAdmin)
