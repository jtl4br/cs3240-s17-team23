# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=50)),
                ('company_phone', models.CharField(max_length=25)),
            ],
            options={
                'permissions': (('create report', 'can create report'),),
            },
        ),
    ]
