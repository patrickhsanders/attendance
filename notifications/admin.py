from django.contrib import admin

from .models import NotificationLog

# Register your models here.
class NotificationLogAdmin(admin.ModelAdmin):
    list_display = ('sender','date','subject', 'fake')
    list_filter = ('recipient','sender','date')
    search_fields = ('recipient','sender','date')

admin.site.register(NotificationLog, NotificationLogAdmin)