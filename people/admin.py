from django.contrib import admin
from .models import Student, ContactInfo, TelephoneNumber, Address, EmergencyContact
from .models import EducationalInformation, EducationalExperience
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email','start_date','course', 'current_project', 'active',"directory_information")
    list_filter = ('course', 'active','current_project',)
    search_fields = ('first_name', 'last_name', 'email',)

# class EducationalInformationAdmin(admin.ModelAdmin):

admin.site.register(Student, StudentAdmin)
admin.site.register(ContactInfo)
admin.site.register(TelephoneNumber)
admin.site.register(Address)
admin.site.register(EmergencyContact)

admin.site.register(EducationalInformation)
admin.site.register(EducationalExperience)
