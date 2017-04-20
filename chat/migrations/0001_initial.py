# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-19 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_recipient', models.CharField(default='RECIPIENT', max_length=25)),
                ('message_content', models.CharField(default='CONTENT', max_length=500)),
                ('message_sender', models.CharField(default='SENDER', max_length=25)),
            ],
        ),
    ]
