from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Account, User, Follow, Review


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'firstname', 'lastname', 'password1', 'password2')


class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'firstname', 'lastname', 'description', 'password1', 'password2', 'account')


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'firstname', 'lastname', 'description', 'account')


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('name', 'description', 'slogan', 'email', 'web', 'phonenumber', 'address', 'cp', 'locality', 'country')


class FollowForm(forms.ModelForm):
    class Meta:
        model = Follow
        fields = ('follower', 'following')
        

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('posted_by', 'posted_to', 'rating')


class ImageForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('image', )