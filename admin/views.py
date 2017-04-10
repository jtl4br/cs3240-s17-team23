from django.shortcuts import render
from registration.models import SiteUser
# Create your views here.
def display_users(request):
    print(SiteUser.objects.all()[0].first_name)
    return render(request, 'Userdisplay.html', {'obj': SiteUser.objects.all()})