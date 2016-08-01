from django.contrib import admin
from .models import Computer, ComputerModel, OperatingSystem, Xcode
# Register your models here.

class ComputerAdmin(admin.ModelAdmin):
    list_display = ('name', 'computer_model')
    list_filter = ('computer_model',)

class ComputerModelAdmin(admin.ModelAdmin):
    list_display = ('computer_model', 'year')
    list_filter = ('computer_model', 'year')

class OperatingSystemAdmin(admin.ModelAdmin):
    list_display = ('friendly_name','granular_name')
    list_filter = ('friendly_name','granular_name')

class XcodeAdmin(admin.ModelAdmin):
    list_display = ('version_number',)
    list_filter = ('version_number',)

admin.site.register(Computer, ComputerAdmin)
admin.site.register(ComputerModel, ComputerModelAdmin)
# admin.site.register(OperatingSystem, OperatingSystemAdmin)
# admin.site.register(Xcode, XcodeAdmin)
