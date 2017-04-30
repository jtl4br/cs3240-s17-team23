# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='user_type',
            field=models.CharField(max_length=7, choices=[('INV_USR', 'Investor'), ('CMP_USR', 'Company')], default='INV_USR'),
        ),
    ]
