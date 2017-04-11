from django.conf.urls import url
from django.contrib import admin

# importing views
# we need to create views.py
from . import views
from registration import views as registration_views
from reports import views as report_views
from admin import views as admin_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # define the url getdata that we have written inside form
    url(r'^signup/', registration_views.signupform),
    url(r'^success/', registration_views.signupform),
    url(r'^login/', registration_views.login_view),
    url(r'^home/', registration_views.home, name='home'),
    url(r'^createreport/', registration_views.reportform),
    url(r'^viewreports/', registration_views.getReports),
    url(r'^uploadfile/', report_views.upload_file),
    url(r'^displayusers/', admin_views.display_users),

    # defining the view for root URL
    url(r'^$', registration_views.login_view),
    url(r'^upload/', report_views.upload_file)
]