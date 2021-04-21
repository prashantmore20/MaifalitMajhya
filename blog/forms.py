from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    contents = forms.CharField(
        widget=forms.Textarea (attrs={
            'rows': '3',
            'placeholder': 'Say Something..!!!',
        }))
    
    image = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ['title', 'contents', 'image']


class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        widget=forms.Textarea (attrs={
            'rows': '3',
            'placeholder': 'Say Something..!!!',
        }))
    class Meta:
        model = Comment
        fields = ['comment']