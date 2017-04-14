from django import forms
from registration.models import SiteUser

class Edit_User_Form(forms.ModelForm):
    class Meta:
        model = SiteUser
        fields = ('admin_status', 'is_active')
