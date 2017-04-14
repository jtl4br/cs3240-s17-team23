from django.shortcuts import render
from registration.models import SiteUser
from .forms import Edit_User_Form
from django.shortcuts import redirect
# Create your views here.
def display_users(request):
    return render(request, 'Userdisplay.html', {'obj': SiteUser.objects.all()})

def edit_user(request, user_id):
    instance = SiteUser.objects.get(id=user_id)
    form = Edit_User_Form(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return render(request, 'Userdisplay.html', {'obj': SiteUser.objects.all()})
    return render(request, 'edituser.html', {'form': form, 'user': instance})