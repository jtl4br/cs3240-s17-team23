from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt
from registration.models import report


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
        
@csrf_exempt
def viewReports_FDA(request):

    reports = report.objects.all()

    for rep in reports:
        print(rep.company_name)

    # Dictionary of report ids to the report attributes
    reportDictionary = {}

    for rep in reports:
        reportDictionary[rep.id] = list()
        reportDictionary[rep.id].append(rep.company_name)
        reportDictionary[rep.id].append(rep.company_phone)
        reportDictionary[rep.id].append(rep.ceo)
        reportDictionary[rep.id].append(rep.company_email)
        reportDictionary[rep.id].append(rep.company_location)
        #reportDictionary[rep.id].append(rep.company_country)
        reportDictionary[rep.id].append(rep.company_sector)
        reportDictionary[rep.id].append(rep.company_industry)
        reportDictionary[rep.id].append(rep.company_projects)


    print(reportDictionary)

    return JsonResponse(reportDictionary, safe=False)

















