from django.contrib.auth.forms import UserCreationForm

from .models import Account


class SignupForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('email', 'name', 'password1', 'password2')