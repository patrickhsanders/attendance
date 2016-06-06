from django import forms
from .models import TelephoneNumber, Address, EmergencyContact

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