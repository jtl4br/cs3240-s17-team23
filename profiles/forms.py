from django import forms
from django.forms import ModelForm

class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=25, required=True)
    password = forms.CharField(label='password', max_length=25, widget=forms.PasswordInput, required=True)