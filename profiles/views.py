from django.shortcuts import render
from django.http import HttpResponseRedirect
from registration.models import SiteUser
from django.contrib.auth import authenticate, login
from .models import UserProfile
from .forms import LoginForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def viewProfile(request, username):
    if 'loggedIn' not in request.session:
        request.session['loggedIn'] = False
    if request.session['loggedIn'] == False:
        form = LoginForm()
        return render(request, 'logintemp.html', {'form': form})

     ### Display all the users you share a group with ###

    myGroups = request.user.groups.all()
    storedUsers = SiteUser.objects.all()  # Get all of the users who have been created
    # Find every user that you are in a group with
    usernamesList = []
    for user in storedUsers:  # Get all users
        otherUserGroups = user.groups.all()  # Get current user's groups
        for group in myGroups:  # iterate through other groups
            for otherGroup in otherUserGroups:  # iterate through every other user's groups
                if str(group.name) == str(otherGroup.name) and user not in usernamesList and request.user.username != user.username:  # Find every person that you share a group with
                    usernamesList.append(user)

    user = SiteUser.objects.get(username=username)
    firstname = request.user.first_name
    lastname = request.user.last_name
    email = request.user.email
    username = request.user.username


    return render(request, 'viewProfile.html', {'firstname':firstname, 'lastname':lastname, 'email':email, 'username':username, 'groupMembers':usernamesList})













