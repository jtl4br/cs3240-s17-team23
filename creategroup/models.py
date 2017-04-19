from django.db import models

# Create your models here.
class group(models.Model):
    group_name = models.CharField(max_length=50)
    group_description = models.CharField(max_length=500)
    creator_name = models.CharField(max_length=50)
    #group_id = models.IntegerField()
    creator_username = models.CharField(max_length=50)

class group_user_pair(models.Model):
    gup_group_name = models.CharField(max_length=50)
    gup_username = models.IntegerField()

class tempModel(models.Model):
    tempModel_name = models.CharField(max_length=50)
    permissions = (
        ("create tempModel", "can create tempModel"),
    )