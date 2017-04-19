from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import NewGroupForm
from django.views.decorators.csrf import csrf_exempt
#from .models import Group
from .models import group
from .models import group_user_pair
from registration.forms import LoginForm

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import tempModel



# Create your views here.
# disabling csrf (cross site request forgery)
@csrf_exempt
def newGroupForm(request):
    if 'loggedIn' not in request.session:
        request.session['loggedIn'] = False
    if request.session['loggedIn'] == False:
        form = LoginForm()
        return render(request, 'logintemp.html', {'form': form})
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        creator = request.session['username']
        context = {
            'name': name,
            'description': description,
            'creator': creator,
        }

        form = NewGroupForm(request.POST)
        if form.is_valid():
            new_group = group()
            new_group.group_name = request.POST['name']
            new_group.group_description = request.POST['description']
            new_group.creator_name = ""
            new_group.creator_username = creator
            new_group.save()
            new_django_group = Group.objects.get_or_create(name='new_group')
            #ct = ContentType.objects.get_for_model(tempModel)
            #permission = Permission.objects.create(codename='can_add_tempModel',
            #                                       name='Can add tempModel',
            #                                       content_type=ct)
            #new_django_group.permissions.add(permission)
            #new_django_group.save()
            #new_group.clear()
            #return render(request, 'groupCreated.html')
            template = loader.get_template('groupCreated.html')
            return HttpResponse(template.render(context, request))
    else:
        # creating a new form
        form = NewGroupForm()
    return render(request, 'createGroup.html', {'form': form})





    # # if post request came
    # if request.method == 'POST':
    #     # getting values from post
    #     name = request.POST.get('name')
    #     description = request.POST.get('description')
    #     creator = "";
    #     #creator = session.username
    #
    #
    #     # adding the values in a context variable
    #     context = {
    #         'name': name,
    #         'description': description,
    #         'creator': creator,
    #     }
    #
    #     # getting our showdata template
    #     template = loader.get_template('groupCreated.html')
    #
    #     # returing the template
    #     return HttpResponse(template.render(context, request))
    # else:
    #     # if post request is not true
    #     # returing the form template
    #     template = loader.get_template('createGroup.html')
    #     return HttpResponse(template.render())