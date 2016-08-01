from django import forms
from .models import Register, ExcusedAbsence
from projects.models import Project
from people.models import Student

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['current_curriculum_project','student']
        widgets = {'student':forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        course = kwargs.pop('course', None)
        super(RegisterForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['current_curriculum_project'].queryset = Project.objects.filter(course=course, deprecated=False).order_by('weight')


class ExcusedAbsenceForm(forms.ModelForm):
    class Meta:
        model = ExcusedAbsence
        exclude = ['note']

    def __init__(self, *args, **kwargs):
        course = kwargs.pop('course', None)
        super(ExcusedAbsenceForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['student'].queryset = Student.objects.filter(active=True).order_by('first_name')