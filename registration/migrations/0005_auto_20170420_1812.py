# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_report_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='timestamp',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='user_type',
            field=models.CharField(choices=[('INV_USR', 'Investor'), ('CMP_USR', 'Company')], max_length=7, default='INV_USR'),
        ),
    ]
