# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20170420_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='timestamp',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
    ]
