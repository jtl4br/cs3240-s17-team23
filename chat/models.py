from django.db import models

class message(models.Model):
    message_recipient = models.CharField(max_length=25, default='RECIPIENT')
    #message_sender = models.CharField(max_length=25)
    message_content = models.CharField(max_length=500, default='CONTENT')
    message_sender = models.CharField(max_length=25, default='SENDER')

    message_encrypted= models.BooleanField(default = False)
