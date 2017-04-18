from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import MessageForm
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def messageform(request):
    if 'loggedIn' not in request.session:
        request.session['loggedIn'] = False
    if request.session['loggedIn'] == False:
        form = LoginForm()
        return render(request, 'logintemp.html', {'form': form})
    

    if request.method == 'POST':

        print("USER TYPE: ", request.user.user_type)
       
        if request.user.user_type == "CMP_USR":
             return render(request, 'cmp_home.html')
        else:
             return render(request, 'inv_home.html')


    elif request.method == "GET":
        return render(request, 'createMessage.html')