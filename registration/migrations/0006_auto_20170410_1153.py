# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20170408_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='admin_status',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='user_type',
            field=models.CharField(default='INV_USR', choices=[('INV_USR', 'Investor'), ('CMP_USR', 'Company')], max_length=7),
        ),
    ]
