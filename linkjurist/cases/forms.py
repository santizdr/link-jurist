from django import forms

from .models import Case

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ('account', 'title', 'description', 'type', 'expiry_date', 'percent')
