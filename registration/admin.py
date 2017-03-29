from django.contrib import admin
from .models import report, SiteUser

# Register your models here.
admin.site.register(report)
admin.site.register(SiteUser)