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
            field=models.CharField(choices=[('CMP_USR', 'Company'), ('INV_USR', 'Investor')], default='INV_USR', max_length=7),
        ),
    ]
