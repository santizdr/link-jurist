from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('account', 'posted_by', 'content')


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content',)
