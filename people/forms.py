from django import forms
from django.forms import Textarea
from ttt.forms import DateInput

from .models import TelephoneNumber, Address, EmergencyContact
from .models import Student, EducationalInformation, EducationalExperience


class TelephoneNumberForm(forms.ModelForm):
    class Meta:
        model = TelephoneNumber
        fields = '__all__'


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'


class EmergencyContactForm(forms.ModelForm):
    class Meta:
        model = EmergencyContact
        fields = ['first_name', "last_name", "relationship"]


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'course', 'start_date','uses_own_laptop']
        widgets = {
            'start_date': DateInput()
        }


class StudentJobStatusNoteForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['job_search_status', ]


class EducationalInformationForm(forms.ModelForm):
    class Meta:
        model = EducationalInformation
        fields = ['has_cs_degree', 'still_a_student']


class EducationalExperienceForm(forms.ModelForm):
    class Meta:
        model = EducationalExperience
        fields = ['degree', 'field_of_study', 'institution', 'start_date', 'end_date']
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput()
        }


class WorkLanguageExperienceForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['programming_language_experience', 'tech_work_experience', 'other_work_experience']
        widgets = {'programming_language_experience': Textarea(attrs={'rows': 2}),
                   'tech_work_experience': Textarea(attrs={'rows': 4}),
                   'other_work_experience': Textarea(attrs={'rows': 4})}
