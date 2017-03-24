from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class SiteUser(AbstractUser):
    USER_CHOICES={
        ('INV_USR', 'Investor'),
        ('CMP_USR', 'Company')
    }
    user_type = models.CharField(
        max_length = 7,
        choices=USER_CHOICES,
        default='INV_USR'
    )