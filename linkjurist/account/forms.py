from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Account, User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'firstname', 'lastname', 'password1', 'password2')


class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'firstname', 'lastname', 'password1', 'password2', 'account')


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('name', 'description', 'slogan', 'email', 'web', 'phonenumber', 'address', 'cp', 'locality', 'country')