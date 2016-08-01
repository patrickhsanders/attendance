from django.forms import ModelForm
from django.forms import Textarea

from .models import Note

class NoteForm(ModelForm):

    class Meta:
        model = Note
        fields = ['text']
        labels = {'text': "Add note"}
        widgets = {'text': Textarea(attrs={'rows':2})}
