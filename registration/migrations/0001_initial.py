# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.validators
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], unique=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, error_messages={'unique': 'A user with that username already exists.'}, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(default='INV_USR', max_length=7, choices=[('INV_USR', 'Investor'), ('CMP_USR', 'Company')])),
                ('admin_status', models.BooleanField(default=0)),
                ('groups', models.ManyToManyField(help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', to='auth.Group', related_query_name='user', blank=True, verbose_name='groups', related_name='user_set')),
                ('user_permissions', models.ManyToManyField(help_text='Specific permissions for this user.', to='auth.Permission', related_query_name='user', blank=True, verbose_name='user permissions', related_name='user_set')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('timestamp', models.DateTimeField(null=True)),
                ('username', models.CharField(default='DEFAULT USERNAME', max_length=150)),
                ('company_name', models.CharField(default='DEFAULT COMPANY', max_length=50)),
                ('company_phone', models.CharField(max_length=11)),
                ('ceo', models.CharField(default='DEFAULT CEO', max_length=25)),
                ('company_email', models.EmailField(default='DEFAULT EMAIL', max_length=100)),
                ('company_location', models.CharField(default='DEFAULT LOC', max_length=25)),
                ('company_country', models.CharField(default='DEFAULT COUNTRY', max_length=25)),
                ('company_sector', models.CharField(default='DEFAULT SECTOR', max_length=25)),
                ('company_industry', models.CharField(default='DEFAULT INDUSTRY', max_length=25)),
                ('company_projects', models.CharField(default='DEFAULT PROJECT', max_length=25)),
                ('delete_item', models.BooleanField(default=False)),
                ('private', models.BooleanField(default=False)),
            ],
            options={
                'permissions': (('create report', 'can create report'),),
            },
        ),
        migrations.CreateModel(
            name='UserFiles',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('file', models.FileField(upload_to='files/users/user.username/%Y_%m_%d/')),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='files',
            field=models.ManyToManyField(null=True, to='registration.UserFiles'),
        ),
    ]
