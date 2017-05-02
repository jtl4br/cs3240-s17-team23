from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import NewGroupForm, LoginForm, Signup
from django.views.decorators.csrf import csrf_exempt
#from .models import Group
from .models import group
from .models import group_user_pair
from registration.forms import LoginForm
from django.contrib.auth.models import Group
from registration.models import SiteUser

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import tempModel

from registration.models import SiteUser



@csrf_exempt
def createGroup(request):
    if 'loggedIn' not in request.session:
        request.session['loggedIn'] = False
    if request.session['loggedIn'] == False:
        form = LoginForm()
        return render(request, 'logintemp.html', {'form': form})


    storedUsers = SiteUser.objects.all()  # Get all of the users who have been created

    if request.method == 'POST':

        groupName = request.POST.get('name')
        groupCreator = request.session['username']
        users = request.POST.get('users')


        groups = Group.objects.all()
        groupExists = False
        for group in groups:
            print(group.name)
            if str(group.name) == str(groupName):
                groupExists = True

        if groupExists == False:
            new_group = Group.objects.create(name=groupName)
            groupUsers = str(users)
            groupUsers = groupUsers.split() # Get list of usernames entered, split on whitespace
            storedUsers = SiteUser.objects.all() # Get all of the users who have been created

            for user in groupUsers:
                userExists = False
                for stUser in storedUsers:
                    if str(user) == str(stUser.username):
                        userExists = True

                if userExists == False:
                    return render(request, 'createGroupFailed.html')


            #Always add the current user, since they made the group
            request.user.groups.add(new_group)

            currentUsername = request.user.username

            if groupExists == False:
                for user in storedUsers:        # The already made users
                    for name in groupUsers:     # The list of usernames entered to be added to the group
                        if user.username == name:
                            user.groups.add(new_group)
            #return render(request, 'viewGroups.html')


        
        # Go back to appropriate viewGroups page
        groups = request.user.groups.all()

        groups.noGroups = True
        for g in groups:
            groups.noGroups = False
            break

        return render(request, 'viewGroups.html', {'groups': groups})
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

    groups.noGroups = True
    for g in groups:
        groups.noGroups = False
        break

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
def RemoveFromGroup(request, group_id, name):

    instance = SiteUser.objects.get(username=name)

    instance.groups.remove(group_id)

    return HttpResponseRedirect('/editgroup/' + group_id + '/')

@csrf_exempt
def addUser(request, group_id):

    if request.method == 'POST':
        name = request.POST.get('newUser')

        storedUsers = SiteUser.objects.all() # Get all of the users who have been created

        userExists = False
        for user in storedUsers:
            if str(user.username) == str(name):
                userExists = True
                break

        if userExists == False:
            id = group_id
            return render(request, 'addUserToGroupFailed.html', {'id': id})

        for user in storedUsers:        # The already made users
            if user.username == name:

                alreadyInGroup = False
                for group in user.groups.all():
                    if str(group.id) == str(group_id):
                        alreadyInGroup = True

                if alreadyInGroup == False:
                    group = user.groups.add(group_id)


        return HttpResponseRedirect('/viewGroups/')
    else:
        id = group_id
        return render(request, 'addUserToGroup.html', {'id': id})
@csrf_exempt
def AdminAddUser(request, group_id):

    if request.method == 'POST':
        name = request.POST.get('newUser')

        storedUsers = SiteUser.objects.all() # Get all of the users who have been created

        print("BEFORE LOOP")
        for user in storedUsers:        # The already made users
            if user.username == name:

                alreadyInGroup = False
                for group in user.groups.all():
                    if str(group.id) == str(group_id):
                        alreadyInGroup = True

                if alreadyInGroup == False:
                    group = user.groups.add(group_id)

        return HttpResponseRedirect('/editgroup/' + group_id + '/')
    else:
        id = group_id
        return render(request, 'adminAddUserToGroup.html', {'id': id})

