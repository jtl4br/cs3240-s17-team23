from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt


### FUNCTIONS FOR INTERACTING WITH THE FDA ###
from django.http import JsonResponse
from django.core import serializers
import json

def login_view_FDA(request):
    context = {}
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            #if user.user_type != None:
            serial = serializers.serialize("json", {"passed": "y"})
            context['Response'] = json.loads(serial)
            return JsonResponse(context, safe=False)

            # A backend authenticated the credentials
        else:
            context['Response'] = 'Failed Login'
            return JsonResponse(context, safe=False)

def viewReports_FDA(request):
    return JsonResponse({'foo':'bar'}, safe=False)