# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFiles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('file', models.FileField(upload_to='files/users/user.username/%Y_%m_%d/')),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='files',
            field=models.ManyToManyField(to='registration.UserFiles'),
        ),
    ]
