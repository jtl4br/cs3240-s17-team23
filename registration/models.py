from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField



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
    username = models.CharField(max_length=150)
    company_name = models.CharField(max_length=50)
    company_phone = PhoneNumberField()
    #company_phone = models.CharField(max_length=25)
    ceo = models.CharField(max_length=25, default='DEFAULT CEO')
    #company_email = models.CharField(max_length=25, default='DEFAULT EMAIL')
    company_email = models.EmailField(max_length=100, default='DEFAULT EMAIL')
    company_location = models.CharField(max_length=25, default='DEFAULT LOC')
    #company_country = models.CharField(max_length=25, default='DEFAULT COUNTRY')
    company_country = CountryField(default='US')
    company_sector = models.CharField(max_length=25, default='DEFAULT SECTOR')
    company_industry = models.CharField(max_length=25, default='DEFAULT INDUSTRY')
    company_projects = models.CharField(max_length=25, default='DEFAULT PROJECT')
    delete_item = models.BooleanField(default = False)
    private = models.BooleanField(default = False)

    class Meta:
    	permissions = (
    		("create report", "can create report"),
    		)