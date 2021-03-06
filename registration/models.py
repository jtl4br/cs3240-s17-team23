from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
#import django.contrib.auth



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
    public_key = models.CharField(max_length= 1000, null=True)
class UserFiles(models.Model):
    #user = models.OneToOneField(User)
    file = models.FileField(upload_to='files/users/user.username/%Y_%m_%d/')

class report(models.Model):

    timestamp = models.DateTimeField(null=True)

    files = models.ManyToManyField(UserFiles, null=True)
    enc_file_op = models.BooleanField(default = False)



    username = models.CharField(max_length=150, default='DEFAULT USERNAME')
    company_name = models.CharField(max_length=50, default='DEFAULT COMPANY')
    #company_phone = PhoneNumberField()
    company_phone = models.CharField(max_length=11)
    ceo = models.CharField(max_length=25, default='DEFAULT CEO')
    #company_email = models.CharField(max_length=25, default='DEFAULT EMAIL')
    company_email = models.EmailField(max_length=100, default='DEFAULT EMAIL')
    company_location = models.CharField(max_length=25, default='DEFAULT LOC')
    company_country = models.CharField(max_length=25, default='DEFAULT COUNTRY')
    #company_country = CountryField(default='US')
    company_sector = models.CharField(max_length=25, default='DEFAULT SECTOR')
    company_industry = models.CharField(max_length=25, default='DEFAULT INDUSTRY')
    company_projects = models.CharField(max_length=25, default='DEFAULT PROJECT')
    delete_item = models.BooleanField(default = False)
    private = models.BooleanField(default = False)

    class Meta:
    	permissions = (
    		("create report", "can create report"),
    		)