from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import File

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file', 'title', 'description', 'price', 'account', 'uploaded_by')

