from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import File

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file', 'title', 'description', 'price', 'account', 'uploaded_by')


    def clean_price(self):
        price = self.cleaned_data['price']
        price_str = str(price)

        parts = price_str.split('.')

        if len(parts[0]) != 3 or len(parts[1]) != 2:
            raise forms.ValidationError("El campo 'price' debe tener 3 dígitos en la parte entera y 2 en la decimal.")

        return price