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
    admin_status = models.BooleanField(default=0)


class report(models.Model):
    company_name = models.CharField(max_length=50)
    company_phone = models.CharField(max_length=25)
    ceo = models.CharField(max_length=25, default='DEFAULT CEO')
    company_email = models.CharField(max_length=25, default='DEFAULT EMAIL')
    company_location = models.CharField(max_length=25, default='DEFAULT LOC')
    company_country = models.CharField(max_length=25, default='DEFAULT COUNTRY')
    company_sector = models.CharField(max_length=25, default='DEFAULT SECTOR')
    company_industry = models.CharField(max_length=25, default='DEFAULT INDUSTRY')
    company_projects = models.CharField(max_length=25, default='DEFAULT PROJECT')

    class Meta:
    	permissions = (
    		("create report", "can create report"),
    		)