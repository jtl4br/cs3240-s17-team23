# importing forms
from django import forms
from django.forms import ModelForm

class MessageForm(forms.Form):
 #does this have to be forms.ModelForm??
    recipient = forms.CharField(label='Recipient', max_length=25, required=True)
    content = forms.CharField(label='Content', max_length=500, required=True)
    encrypted = forms.BooleanField(label='Encrypted', required = False)
    #sender = forms.CharField(label='Content', max_length=500, required=True)

# creating our forms
class Signup(forms.Form):
    # django gives a number of predefined fields
    # CharField and EmailField are only two of them
    # go through the official docs for more field details
    firstname = forms.CharField(label='Enter your first name', max_length=25, required=True)
    lastname = forms.CharField(label='Enter your last name', max_length=25, required=True)
    email = forms.EmailField(label='Enter your email', max_length=100,required=True)
    username = forms.CharField(label='Enter a user name', max_length=25, required=True)
    password = forms.CharField(label='Enter a password', max_length=25, widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Confirm your password', max_length=25, widget=forms.PasswordInput, required=True)
    Type = forms.ChoiceField(label='Type of User', choices=[('INV_USR', 'Investor'),('CMP_USR', 'Company')])

class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=25, required=True)
    password = forms.CharField(label='password', max_length=25, widget=forms.PasswordInput, required=True)

class Upload(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
