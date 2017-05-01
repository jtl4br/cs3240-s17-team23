from django.db import models
from registration.models import SiteUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(SiteUser, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    username = models.CharField(max_length=50, blank=True)

    @receiver(post_save, sender=SiteUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=SiteUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

#SiteUser.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])