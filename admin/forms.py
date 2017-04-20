from django import forms
from registration.models import SiteUser
from registration.models import report

class Edit_User_Form(forms.ModelForm):
    class Meta:
        model = SiteUser
        fields = ('admin_status', 'is_active')

class Edit_Report_Form(forms.ModelForm):
	class Meta:
		model = report 
		exclude = (None,)
