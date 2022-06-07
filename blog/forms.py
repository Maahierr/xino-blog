from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class' : 'form-title', 'placeholder' : 'Enter Title For Blog'}),
            'author': forms.TextInput(attrs={'class' : 'form-author', 'value' : '', 'type' : 'hidden', 'id':'user'}),
            'body': forms.Textarea(attrs={'class' : 'form-body', 'placeholder' : 'Enter Body For Blog', 'rows' : '10'}),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-title', 'placeholder':'Enter Title For Blog'}),
            'body': forms.Textarea(attrs={'class': 'form-body', 'placeholder':'Enter Body; You Can Also For Blog And Can Write HTML In Body', 'rows':'10'}),
        }