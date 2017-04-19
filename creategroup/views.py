from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import NewGroupForm, LoginForm, Signup
from django.views.decorators.csrf import csrf_exempt
from .models import group
from .models import group_user_pair
from registration.forms import LoginForm
from django.contrib.auth.models import Group
from registration.models import SiteUser


# # Create your views here.
# # disabling csrf (cross site request forgery)
# @csrf_exempt
# def newGroupForm(request):
#     if 'loggedIn' not in request.session:
#         request.session['loggedIn'] = False
#     if request.session['loggedIn'] == False:
#         form = LoginForm()
#         return render(request, 'logintemp.html', {'form': form})
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         creator = request.session['username']
#         context = {
#             'name': name,
#             'description': description,
#             'creator': creator,
#         }

#         form = NewGroupForm(request.POST)
#         if form.is_valid():
#             new_group = group()
#             new_group.group_name = request.POST['name']
#             new_group.group_description = request.POST['description']
#             new_group.creator_name = ""
#             new_group.creator_username = creator
#             new_group.save()
#             #return render(request, 'groupCreated.html')
#             template = loader.get_template('groupCreated.html')
#             return HttpResponse(template.render(context, request))
#     else:
#         # creating a new form
#         form = NewGroupForm()
#     return render(request, 'createGroup.html', {'form': form})


@csrf_exempt
def createGroup(request):
    if 'loggedIn' not in request.session:
        request.session['loggedIn'] = False
    if request.session['loggedIn'] == False:
        form = LoginForm()
        return render(request, 'logintemp.html', {'form': form})

    if request.method == 'POST':
        groupName = request.POST.get('name')
        groupCreator = request.session['username']
        users = request.POST.get('users')

        new_group = Group.objects.create(name=groupName)

        groupUsers = str(users)
        groupUsers = groupUsers.split() # Get list of usernames entered, split on whitespace

        storedUsers = SiteUser.objects.all() # Get all of the users who have been created

        #Always add the current user, since they made the group
        request.user.groups.add(new_group)

        for user in storedUsers:        # The already made users
            for name in groupUsers:     # The list of usernames entered to be added to the group
                if user.username == name:
                    print("added a new person!!!!!!!")
                    user.groups.add(new_group)
        
        # Go back to appropriate home page
        if request.user.user_type == "CMP_USR":
             return render(request, 'cmp_home.html')
        else:
             return render(request, 'inv_home.html')
             
    else:
        form = NewGroupForm()
    return render(request, 'createGroup.html', {'form': form})


@csrf_exempt
def viewGroups(request):
    if 'loggedIn' not in request.session:
        request.session['loggedIn'] = False
    if request.session['loggedIn'] == False:
        form = LoginForm()
        return render(request, 'logintemp.html', {'form': form})

    groups = request.user.groups.all()
    
    print(groups)

    return render(request, 'viewGroups.html', {'groups': groups})


@csrf_exempt
def leaveGroup(request, group_id):

    currentUser = request.user

    currentUser.groups.remove(group_id)

    # Go back to appropriate home page
    if request.user.user_type == "CMP_USR":
        return render(request, 'cmp_home.html')
    else:
        return render(request, 'inv_home.html')

@csrf_exempt
def addUser(request, group_id):

    if request.method == 'POST':
        name = request.POST.get('newUser')

        storedUsers = SiteUser.objects.all() # Get all of the users who have been created

        print("BEFORE LOOP")
        for user in storedUsers:        # The already made users
            if user.username == name:
                print("MADE IT BEFORE IF: ", user.username)

                alreadyInGroup = False
                # print()
                # for group in user.groups.all():
                #     if group.id == group_id:
                #         alreadyInGroup = True

                print("Already in group?: ", alreadyInGroup)

                group = user.groups.add(group_id)
                for group in user.groups.all():
                     print(group.name)
                

        return HttpResponseRedirect('/viewGroups/')
    else:
        id = group_id
        return render(request, 'addUserToGroup.html', {'id': id})














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