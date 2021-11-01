from django import forms
from django.db.models import fields
from django.forms.models import ModelForm
from .models import Comment

# will work on it ltr


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)
# end email form


class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('name', 'email', 'body')
