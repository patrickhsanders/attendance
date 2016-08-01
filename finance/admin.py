from django.contrib import admin
from .models import StudentTuition, Payment
# Register your models here.
# class NoteAdmin(admin.ModelAdmin):
#     list_display = ('text','author','date_added','last_modified')
#     list_filter = ('author',)

admin.site.register(StudentTuition)

admin.site.register(Payment)