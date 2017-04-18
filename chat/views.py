from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import MessageForm, LoginForm, Signup
from .models import message 
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

        form = MessageForm(request.POST)
        if form.is_valid():
            new_message = message()
            new_message.message_recipient = request.POST.get("recipient")
            new_message.message_content = request.POST.get("content")
            new_message.save()

            # report = form.save()
            # report.message_recipient = request.POST.get("recipient")
            # report.message_content = request.POST.get("content")
            # report.save()
            return render(request, 'cmp_home.html')

        # Go back to appropriate home page
        if request.user.user_type == "CMP_USR":
             return render(request, 'cmp_home.html')
        else:
             return render(request, 'inv_home.html')

    elif request.method == "GET":
        form = MessageForm(request.GET)
        return render(request, 'createMessage.html', {'form': form})