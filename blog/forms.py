from django import forms
from .models import Post, Category, Comment, HashTag


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['category', 'title', 'content']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(
                attrs={'rows': '3', 'cols': '110', 'placeholder': '댓글을 입력해주세요.', 'style': 'resize:none'})
        }


class HashTagForm(forms.ModelForm):

    class Meta:
        model = HashTag
        fields = ['name']
