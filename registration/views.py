from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Signup, LoginForm, ReportForm
from .models import SiteUser
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView

# Create your views here.

def signupform(request):
    # if form is submitted
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            if request.POST['password'] != request.POST['password2']:
                return render(request, 'signupform.html', {'response': 'Passwords do not match', 'form': form})
            user = SiteUser.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            user.first_name = request.POST['firstname']
            user.last_name = request.POST['lastname']
            user.user_type = request.POST['Type']
            return render(request, 'success.html')
    else:
    # creating a new form
        form = Signup()
    return render(request, 'signupform.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return render(request, 'home.html')
            # A backend authenticated the credentials
            else:
                return render(request, 'logintemp.html', {'response': 'Invalid Login', 'form': form})
        # No backend authenticated the credentials



    else:
        form = LoginForm()
    return render(request, 'logintemp.html', {'form': form})

def home(request):
    return render(request, 'home.html')


def reportform(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save()
            report.name = request.POST.get("company_name", '')
            report.num = request.POST.get("company_phone", '')
            report.save()
            return render(request, 'home.html')
    elif request.method == "GET":
        form = ReportForm(request.GET)
        return render(request, 'reports.html', {'form': form})

# still need to put in function from somewhere import handle_uploaded_file











