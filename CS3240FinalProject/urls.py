from django.conf.urls import url
from django.contrib import admin

# importing views
# we need to create views.py
from . import views
from registration import views as registration_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # define the url getdata that we have written inside form
    url(r'^signup/', registration_views.signupform),
    url(r'^success/', registration_views.signupform),
    url(r'^login/', registration_views.login_view),
    url(r'^home/', registration_views.home, name='home'),
    url(r'^createreport/', registration_views.reportform),


    # defining the view for root URL
    url(r'^$', registration_views.login_view),
]