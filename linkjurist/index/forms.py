from django import forms
from .models import Post, PostLike


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('account', 'posted_by', 'content')


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content',)


class PostLikeForm(forms.ModelForm):
    class Meta:
        model = PostLike
        fields = ('user', 'post')

