# importing forms
from django import forms


# creating our forms
class NewGroupForm(forms.Form):
    # django gives a number of predefined fields
    # CharField and EmailField are only two of them
    # go through the official docs for more field details
    name = forms.CharField(label='Enter a group name', max_length=100)
    description = forms.CharField(label='Enter a group description', max_length=700)