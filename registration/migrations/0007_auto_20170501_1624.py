# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-01 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_auto_20170501_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='user_type',
            field=models.CharField(choices=[('INV_USR', 'Investor'), ('CMP_USR', 'Company')], default='INV_USR', max_length=7),
        ),
    ]
