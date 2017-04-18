# importing forms
from django import forms

class MessageForm(forms.Form):
    recipient = forms.CharField(label='Recipient', max_length=25, required=True)
    content = forms.CharField(label='Content', max_length=500, required=True)