import datetime
from django import forms
from .models import Case, Apply


class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ('account', 'title', 'description', 'type', 'expiry_date')

    def clean_expiry_date(self):
        expiry_date = self.cleaned_data['expiry_date']
        if expiry_date and expiry_date <= datetime.date.today():
            raise forms.ValidationError("La fecha de vencimiento debe ser posterior a la fecha actual.")
        return expiry_date
    

class EditCaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ('title', 'description', 'type', 'expiry_date')

    def clean_expiry_date(self):
        expiry_date = self.cleaned_data['expiry_date']
        if expiry_date and expiry_date <= datetime.date.today():
            raise forms.ValidationError("La fecha de vencimiento debe ser posterior a la fecha actual.")
        return expiry_date


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ('applicant', 'case')