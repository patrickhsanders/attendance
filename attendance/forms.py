from django import forms
from .models import Register
from projects.models import Project

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['current_curriculum_project','student']
        widgets = {'student':forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        course = kwargs.pop('course', None)
        super(RegisterForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['current_curriculum_project'].queryset = Project.objects.filter(course=course).order_by('weight')

