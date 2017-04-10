from django.contrib import admin
from .models import group, group_user_pair

# Register your models here.
admin.site.register(group)
admin.site.register(group_user_pair)