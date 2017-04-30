from django.shortcuts import render
from registration.models import SiteUser
from django.contrib.auth.models import Group
from .forms import Edit_User_Form
from django.shortcuts import redirect
from registration.models import report
from .forms import Edit_Report_Form
from .forms import Edit_Group_Form
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def display_users(request):
    return render(request, 'Userdisplay.html', {'obj': SiteUser.objects.all()})
def display_groups(request):
    return render(request, 'GroupDisplay.html', {'grp': Group.objects.all()})

def edit_user(request, user_id):
    instance = SiteUser.objects.get(id=user_id)
    form = Edit_User_Form(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return render(request, 'Userdisplay.html', {'obj': SiteUser.objects.all()})
    return render(request, 'edituser.html', {'form': form, 'user': instance})

def edit_form(request, form_id):
    instance = report.objects.get(id=form_id)
    form = Edit_Report_Form(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/viewreports/')
    return render(request, 'editform.html', {'form': form, 'report': instance})

def edit_group(request, group_id):
    instance = Group.objects.get(id=group_id)
    members = []
    user_instance = SiteUser.objects.all()
    for i in user_instance:
        if i.groups.filter(name = instance.name).exists():
            members.append(i)

    form = Edit_Group_Form(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('/displaygroups/')
    return render(request, 'editgroup.html', {'form': form, 'group': instance, 'members': members})

@csrf_exempt
def deleteGroup(request, group_id):

    currentUser = request.user

    currentUser.groups.remove(group_id)

    if request.user.user_type == "CMP_USR":
        return render(request, 'cmp_home.html')
    else:
        return render(request, 'inv_home.html')