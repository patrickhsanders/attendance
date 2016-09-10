from django import forms
from ttt.forms import DateInput
from .models import Recruit, Company, Job, Task, Resume, Link


class RecruitForm(forms.ModelForm):
    class Meta:
        model = Recruit
        fields = ['wants_help_looking_for_work']


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'website', 'city']


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'salary', 'start_date', 'end_date', 'company']
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'other', 'date_to_finish_by', 'completed']
        widgets = {
            'date_to_finish_by':DateInput()
        }


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['file']


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = '__all__'
