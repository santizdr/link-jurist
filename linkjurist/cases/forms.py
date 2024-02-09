import datetime
from django import forms
from .models import Case, Apply

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ('account', 'title', 'description', 'type', 'expiry_date', 'percent')

    def clean_percent(self):
        percent = self.cleaned_data['percent']
        if not (0 <= percent <= 99):
            raise forms.ValidationError("El campo 'percent' debe ser un número entre 0 y 99.")
        return percent

    def clean_expiry_date(self):
        expiry_date = self.cleaned_data['expiry_date']
        if expiry_date and expiry_date <= datetime.date.today():
            raise forms.ValidationError("La fecha de vencimiento debe ser posterior a la fecha actual.")
        return expiry_date
    

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ('applicant', 'case')