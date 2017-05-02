from django.conf.urls import url
from django.contrib import admin

# importing views
# we need to create views.py
from django.conf import settings
from django.conf.urls.static import static
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
from profiles import views as profiles_views

import django.contrib.auth

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
    url(r'^displaygroups/', admin_views.display_groups),
    url(r'^edituser/(.*)/', admin_views.edit_user),
    url(r'^search/', registration_views.search),
    url(r'^editreport/(.*)/', admin_views.edit_form),
    url(r'^editgroup/(.*)/', admin_views.edit_group),
    url(r'^deletereport/(?P<form_id>[0-9]+)$', admin_views.deleteReport),

    url(r'^advancedSearch/', registration_views.advancedSearch),

    # defining the view for root URL
    url(r'^$', registration_views.login_view),
    url(r'^upload/', report_views.upload_file),

    url(r'^createGroup/', creategroup_views.createGroup),
    url(r'^viewGroups/', creategroup_views.viewGroups),
    url(r'^leaveGroup/(?P<group_id>[0-9]+)$', creategroup_views.leaveGroup),
    url(r'^removeFromGroup/(.*)/(.*)/', creategroup_views.RemoveFromGroup),
    url(r'^addUser/(?P<group_id>[0-9]+)$', creategroup_views.addUser),
    url(r'^addUserAdmin/(?P<group_id>[0-9]+)$', creategroup_views.AdminAddUser),

    url(r'^createmessage/', chat_views.messageform),
    url(r'^viewmessages/', chat_views.viewMessages),
    url(r'^deletemessage/(?P<message_id>[0-9]+)$', chat_views.deleteMessage),

    ### URLs FOR THE FDA ###
    url(r'^login_FDA/$', FDA_views.login_view_FDA),
    url(r'^viewReports_FDA/', FDA_views.viewReports_FDA),
    #url(r'^stuff/', FDA_views.profile),
    url(r'^viewReport_FDA/', FDA_views.viewReport_FDA),

    url(r'^keyupload/(?P<message_id>[0-9]+)$', chat_views.decrypt),
    url(r'^encrypt_FDA/', FDA_views.encrypt_FDA),
    url(r'^download_file/(?P<file_id>[0-9]+)$', FDA_views.download),

    url(r'^profile/(?P<username>[a-zA-Z0-9]+)$', profiles_views.viewProfile),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

