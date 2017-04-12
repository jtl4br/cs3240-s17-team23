# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='user_type',
            field=models.CharField(max_length=7, default='INV_USR', choices=[('CMP_USR', 'Company'), ('INV_USR', 'Investor')]),
        ),
    ]
