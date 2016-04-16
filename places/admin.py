from django.contrib import admin
from .models import Place
# Register your models here.

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('frond','seat','student','computer')
    list_filter = ('frond',)

admin.site.register(Place, PlaceAdmin)
