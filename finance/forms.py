from django import forms
from django.forms import Textarea

from .models import Payment, StudentTuition

class StudentTuitionForm(forms.ModelForm):
    class Meta:
        model = StudentTuition
        fields = ['tuition_total', 'payed_in_full']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['date','amount','type','completed']