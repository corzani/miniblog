from django import forms

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=100)
    body = forms.CharField()
    tags = forms.CharField()
