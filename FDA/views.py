

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt
from registration.models import report
from CS3240FinalProject import settings

### FUNCTIONS FOR INTERACTING WITH THE FDA ###
from django.http import JsonResponse
from django.core import serializers
import json
from django.utils.encoding import smart_str
import os
import mimetypes
from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper


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
        reportFiles = list()
        reportDictionary[rep.id] = list()
        reportDictionary[rep.id].append(rep.company_name)
        reportDictionary[rep.id].append(rep.company_phone)
        reportDictionary[rep.id].append(rep.ceo)
        reportDictionary[rep.id].append(rep.company_email)
        reportDictionary[rep.id].append(rep.company_location)
        # reportDictionary[rep.id].append(rep.company_country)
        reportDictionary[rep.id].append(rep.company_sector)
        reportDictionary[rep.id].append(rep.company_industry)
        reportDictionary[rep.id].append(rep.company_projects)
        for file in rep.files.all():
            reportFiles.append(file.file.name)
        reportDictionary[rep.id].append(reportFiles)

    print(reportDictionary)

    return JsonResponse(reportDictionary, safe=False)


@csrf_exempt
def viewReport_FDA(request):
    reportID = request.POST.get('reportID')
    reports = report.objects.all()

    # dictionary to hold the single report
    singleReport = {}
    reportFiles = list()

    for rep in reports:
        if str(rep.id) == str(reportID):
            singleReport[rep.id] = list()
            singleReport[rep.id].append(rep.company_name)
            singleReport[rep.id].append(rep.company_phone)
            singleReport[rep.id].append(rep.ceo)
            singleReport[rep.id].append(rep.company_email)
            singleReport[rep.id].append(rep.company_location)
            # reportDictionary[rep.id].append(rep.company_country)
            singleReport[rep.id].append(rep.company_sector)
            singleReport[rep.id].append(rep.company_industry)
            singleReport[rep.id].append(rep.company_projects)
            for file in rep.files.all():
                reportFiles.append(file.file.name)
            singleReport[rep.id].append(reportFiles)

    print(singleReport)

    return JsonResponse(singleReport, safe=False)

def download(request,file_name):
    file_path = settings.MEDIA_ROOT +'/'+ file_name
    file_wrapper = FileWrapper(file(file_path,'rb'))
    file_mimetype = mimetypes.guess_type(file_path)
    response = HttpResponse(file_wrapper, content_type=file_mimetype )
    response['X-Sendfile'] = file_path
    response['Content-Length'] = os.stat(file_path).st_size
    response['Content-Disposition'] = 'attachment; filename=%s/' % smart_str(file_name)
    return response


def encrypt_FDA(request):
    print("done!")










































