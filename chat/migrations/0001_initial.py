# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('message_recipient', models.CharField(default='RECIPIENT', max_length=25)),
                ('message_content', models.CharField(default='CONTENT', max_length=500)),
                ('message_sender', models.CharField(default='SENDER', max_length=25)),
                ('message_encrypted', models.BooleanField(default=False)),
            ],
        ),
    ]
