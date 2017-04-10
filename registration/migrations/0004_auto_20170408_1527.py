# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20170403_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='user_type',
            field=models.CharField(default='INV_USR', choices=[('INV_USR', 'Investor'), ('CMP_USR', 'Company')], max_length=7),
        ),
    ]
