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

    user = SiteUser.objects.get(username=username)
    firstname = request.user.first_name
    lastname = request.user.last_name
    email = request.user.email
    username = request.user.username

    return render(request, 'viewProfile.html', {'firstname':firstname, 'lastname':lastname, 'email':email, 'username':username})