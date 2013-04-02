from django import forms
from django.core.exceptions import ValidationError

def validate_not_empty(value):
    if value.strip() == "":
        raise ValidationError('This field cannot be empty')

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=100,label="Post title",validators=[validate_not_empty])
    body = forms.CharField(label="Post content",validators=[validate_not_empty],widget = forms.Textarea)
    tags = forms.CharField(label="Tags*",required=False)

class AddCommentForm(forms.Form):
    comment = forms.CharField(label="Add a comment",validators=[validate_not_empty],widget = forms.Textarea)