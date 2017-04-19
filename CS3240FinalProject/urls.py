from django.conf.urls import url
from django.contrib import admin

# importing views
# we need to create views.py
from . import views
from registration import views as registration_views
from FDA import views as FDA_views
from reports import views as report_views
from creategroup import views as creategroup_views
from admin import views as admin_views
from django.conf.urls import url
from django.contrib import admin
from admin import views as admin_views
from chat import views as chat_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # define the url getdata that we have written inside form
    url(r'^signup/', registration_views.signupform),
    url(r'^success/', registration_views.signupform),
    url(r'^login/', registration_views.login_view),
    url(r'^home/', registration_views.home, name='home'),
    url(r'^createreport/', registration_views.reportform),
    url(r'^logout/', registration_views.logout),
    url(r'^viewreports/', registration_views.getReports),
    url(r'^uploadfile/', report_views.upload_file),
    url(r'^displayusers/', admin_views.display_users),
    url(r'^edituser/(.*)/', admin_views.edit_user),
    url(r'^search/', registration_views.search),
    url(r'^editreport/(.*)/', admin_views.edit_form),

    url(r'^advancedSearch/', registration_views.advancedSearch),

    # defining the view for root URL
    url(r'^$', registration_views.login_view),
    url(r'^upload/', report_views.upload_file),

    url(r'^createGroup/', creategroup_views.createGroup),
    url(r'^viewGroups/', creategroup_views.viewGroups),
    url(r'^leaveGroup/(?P<group_id>[0-9]+)$', creategroup_views.leaveGroup),
    url(r'^addUser/(?P<group_id>[0-9]+)$', creategroup_views.addUser),

    url(r'^createmessage/', chat_views.messageform),
    url(r'^viewmessages/', chat_views.viewMessages),

    ### URLs FOR THE FDA ###
    url(r'^login_FDA/', FDA_views.login_view_FDA),
    url(r'^viewReports_FDA/', FDA_views.viewReports_FDA),



]   

