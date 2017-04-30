from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt


### FUNCTIONS FOR INTERACTING WITH THE FDA ###
from django.http import JsonResponse
from django.core import serializers
import json

from django.http import HttpResponse

@csrf_exempt
def login_view_FDA(request):
   

    username = request.POST.get('username')
    password = request.POST.get('password')

    print("USER: ", username)
    print("PASS: ", password)

    user = authenticate(username=username, password=password)

    # user = authenticate(username, password)
    if user is not None:
        data = {
            'passed': 'y',
        }
        return JsonResponse(data, safe=False)
    else:
        data = {
            'passed': 'n',
        }
        return JsonResponse(data, safe=False)
        

    

# def login_view_FDA(request):
#     context = {}

#     print("HERE 1")

#     if request.method == 'POST':

#         print("HERE")

#         user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
#         if user is not None:
#             #if user.user_type != None:
#             data = {"passed": "y"}
           
#             return JsonResponse(data)
#         else:
#             data = {"passed": "y"}
#             return JsonResponse(data)

def viewReports_FDA(request):
    return JsonResponse({'foo':'bar'}, safe=False)