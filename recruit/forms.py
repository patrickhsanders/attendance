from django import forms
from .models import Recruit, Company, Job, Task, Resume


class RecruitForm(forms.ModelForm):
    class Meta:
        model = Recruit
        fields = ['wants_help_looking_for_work']

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'website', 'url']

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'salary', 'start_date', 'end_date', 'company']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'other', 'date_to_finish_by']

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['file']