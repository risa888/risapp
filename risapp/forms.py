from django import forms
from .models import Post,Comments
# from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'photo',
            'caption',
            'tag_name'
        ]

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = [
            'comment',
            'user',
            'post'
        ]

