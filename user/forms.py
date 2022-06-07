from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class signup(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-user'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-password'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-password', 'placeholder' : 'Re-Enter Your Password For Confirmation'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-email'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')