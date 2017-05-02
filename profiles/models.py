from django.db import models
from registration.models import SiteUser
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(SiteUser, on_delete=models.CASCADE)



#SiteUser.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])