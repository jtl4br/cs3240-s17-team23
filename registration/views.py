from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Signup, LoginForm, ReportForm
from .models import SiteUser, report, UserFiles
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt
import datetime

from django.db.models import Q

# Create your views here.

def signupform(request):
    # if form is submitted
    if 'loggedIn' not in request.session:
        request.session['loggedIn'] = False
    if request.session['loggedIn'] == True:
        return home(request)
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            if request.POST['password'] != request.POST['password2']:
                return render(request, 'signupform.html', {'response': 'Passwords do not match', 'form': form})
            userCheck = request.POST['username']
            check = SiteUser.objects.filter(username=userCheck)
            if check.exists():
                return render(request, 'signupform.html', {'response': 'Username Taken', 'form': form})
            user = SiteUser.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            user.first_name = request.POST['firstname']
            user.last_name = request.POST['lastname']
            user.user_type = request.POST['Type']
            user.save()
            request.session['username'] = request.POST['username']
            request.session['user_type'] = user.user_type
            request.session['loggedIn'] = True
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, user)
            return render(request, 'success.html')
    else:
    # creating a new form
        form = Signup()
    return render(request, 'signupform.html', {'form': form})

def login_view(request):
    check = SiteUser.objects.filter(username='Admin')
    if not check.exists():
        user = SiteUser.objects.create_user('Admin', 'admin@gmail.com', 'Admin')
        user.first_name = 'Administrator'
        user.last_name = 'Account'
        user.user_type = 'INV_USR'
        user.admin_status = True
        user.save()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None and user.is_active is True:
                login(request, user)
                request.session['username'] = request.POST['username']
                request.session['user_type'] = user.user_type
                request.session['loggedIn'] = True
                if user.user_type != None:
                    if user.user_type == 'INV_USR':
                        return render(request, 'inv_home.html')
                    elif user.user_type == 'CMP_USR':
                        return render(request, 'cmp_home.html')
                return render(request, 'home.html')

            # A backend authenticated the credentials
            else:
                return render(request, 'logintemp.html', {'response': 'Invalid Login', 'form': form})
        # No backend authenticated the credentials

    else:
        if 'loggedIn' not in request.session:
            request.session['loggedIn'] = False
        if request.session['loggedIn'] == True:
            return home(request)
        else:
            form = LoginForm()
            return render(request, 'logintemp.html', {'form': form})

def home(request):
    if 'loggedIn' not in request.session:
        request.session['loggedIn'] = False
    if request.session['loggedIn'] == False:
        form = LoginForm()
        return render(request, 'logintemp.html', {'form': form})
    user_type = request.session['user_type']
    if user_type != None:
        if user_type == 'INV_USR':
            return render(request, 'inv_home.html')
        elif user_type == 'CMP_USR':
            return render(request, 'cmp_home.html')
    return render(request, 'home.html')

def logout(request):
    user = None
    request.session['username'] = None
    request.session['user_type'] = None
    request.session['loggedIn'] = False
    form = LoginForm()
    return render(request, 'logintemp.html', {'form': form})


def reportform(request):
    if 'loggedIn' not in request.session:
        request.session['loggedIn'] = False
    if request.session['loggedIn'] == False:
        form = LoginForm()
        return render(request, 'logintemp.html', {'form': form})
    if request.session['user_type'] == "INV_USR":
        return render(request, 'inv_home.html')
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            report = form.save()
            report.username = request.user.username
            report.name = request.POST.get("company_name", '')
            report.num = request.POST.get("company_phone", '')
            report.ceo = request.POST.get("ceo", '')
            report.email = request.POST.get("company_email", '')
            report.location = request.POST.get("company_location", '')
            report.country = request.POST.get("company_country", '')
            report.sector = request.POST.get("company_sector", '')
            report.industry = request.POST.get("company_industry", '')
            report.projects = request.POST.get("company_projects", '')
            report.private = request.POST.get("private", '')
            report.timestamp = datetime.datetime.now()
            report.save()
            files = request.FILES.getlist('file_field')

            for f in files:
                file = UserFiles.objects.create(file=f)
                report.files.add(file)
                file.save()
            report.save()
            print(report.timestamp)
            return render(request, 'cmp_home.html')
        else:
            return render(request, 'reports.html', {'form': form})
    else:
        form = ReportForm(request.GET)
        return render(request, 'reports.html', {'form': form})

def getReports(request):
    user = request.user
    for each in report.objects.all():
        if each.delete_item is True:
            each.delete()

    reports = report.objects.all()
    listReports = []

    for rep in reports:
        if rep.private == False or user.admin_status:
            listReports.append(rep)

    myGroups = request.user.groups.all()

    storedUsers = SiteUser.objects.all()  # Get all of the users who have been created

    # Find every user that you are in a group with
    usernamesList = []
    for user in storedUsers:  # Get all users
        otherUserGroups = user.groups.all()  # Get current user's groups
        for group in myGroups:  # iterate through other groups
            for otherGroup in otherUserGroups:  # iterate through every other user's groups
                if str(group.name) == str(
                        otherGroup.name) and user not in usernamesList:  # Find every person that you share a group with
                    usernamesList.append(user)

    # for username in usernamesList:
    #     print("I share a group with: ", username)

    # Display public reports and only private reports from group members
    for rep in reports:
        if rep.private == False:
            listReports.append(rep)
        else:
            print(rep.username)
            if str(rep.username) in str(usernamesList):
                print("dislay private report from: ", rep.username)
                listReports.append(rep)
    return render(request, 'viewReports.html', {'reports': listReports})

@csrf_exempt
def search(request):
    user = request.user
    if request.method == 'POST':
        searchBar = request.POST.get('search')

        reports = report.objects.filter(Q(company_name__contains=searchBar)|Q(company_phone__contains=searchBar)|
                                        Q(company_industry__contains=searchBar)|Q(company_email__contains=searchBar)|
                                        Q(company_location__contains=searchBar)|Q(company_projects__contains=searchBar))
        listReports = []

        for rep in reports:
             if rep.private == False or user.admin_status:
                 listReports.append(rep)

        myGroups = request.user.groups.all()

        storedUsers = SiteUser.objects.all()  # Get all of the users who have been created

        # Find every user that you are in a group with
        usernamesList = []
        for user in storedUsers:  # Get all users
            otherUserGroups = user.groups.all()  # Get current user's groups
            for group in myGroups:  # iterate through other groups
                for otherGroup in otherUserGroups:  # iterate through every other user's groups
                    if str(group.name) == str(
                            otherGroup.name) and user not in usernamesList:  # Find every person that you share a group with
                        usernamesList.append(user)

        # for username in usernamesList:
        #     print("I share a group with: ", username)

        # Display public reports and only private reports from group members
        for rep in reports:
            if rep.private == False:
                listReports.append(rep)
            else:
                print(rep.username)
                if str(rep.username) in str(usernamesList):
                    print("dislay private report from: ", rep.username)
                    listReports.append(rep)
        return render(request, 'viewReports.html', {'reports': listReports})


@csrf_exempt
def advancedSearch(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        industry = request.POST.get('industry')
        email = request.POST.get('email')
        location = request.POST.get('location')
        projects = request.POST.get('projects')

        set = report.objects.filter()

        if name != None:
            set = set & report.objects.filter(company_name__contains=name)

        if number != None:
            set = set & report.objects.filter(company_phone__contains=number)

        if industry != None:
            set = set & report.objects.filter(company_industry__contains=industry)

        if email != None:
            set = set & report.objects.filter(company_email__contains=email)

        if location != None:
            set = set & report.objects.filter(company_location__contains=location)

        if projects != None:
            set = set & report.objects.filter(company_projects__contains=projects)

        # finalListReports = []
        # for rep in set:
        #     if rep.private == False:
        #         finalListReports.append(rep)

        listReports = []
        myGroups = request.user.groups.all()
        storedUsers = SiteUser.objects.all()  # Get all of the users who have been created

        # Find every user that you are in a group with
        usernamesList = []
        for user in storedUsers:  # Get all users
            otherUserGroups = user.groups.all()  # Get current user's groups
            for group in myGroups:  # iterate through other groups
                for otherGroup in otherUserGroups:  # iterate through every other user's groups
                    if str(group.name) == str(
                            otherGroup.name) and user not in usernamesList:  # Find every person that you share a group with
                        usernamesList.append(user)

        # Display public reports and only private reports from group members
        for rep in set:
            if rep.private == False or user.admin_status:
                listReports.append(rep)
            else:
                if str(rep.username) in str(usernamesList):
                    listReports.append(rep)

        return render(request, 'viewReports.html', {'reports': listReports})

    else:
        return render(request, 'advancedSearch.html')



    













