# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields
import django.utils.timezone
import django.core.validators
import django_countries.fields
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('username', models.CharField(validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], max_length=30, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', verbose_name='username', unique=True, error_messages={'unique': 'A user with that username already exists.'})),
                ('first_name', models.CharField(verbose_name='first name', max_length=30, blank=True)),
                ('last_name', models.CharField(verbose_name='last name', max_length=30, blank=True)),
                ('email', models.EmailField(verbose_name='email address', max_length=254, blank=True)),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(default='INV_USR', max_length=7, choices=[('CMP_USR', 'Company'), ('INV_USR', 'Investor')])),
                ('admin_status', models.BooleanField(default=0)),
                ('groups', models.ManyToManyField(to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(to='auth.Permission', blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'users',
                'abstract': False,
                'verbose_name': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(null=True)),
                ('username', models.CharField(default='DEFAULT USERNAME', max_length=150)),
                ('company_name', models.CharField(default='DEFAULT COMPANY', max_length=50)),
                ('company_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('ceo', models.CharField(default='DEFAULT CEO', max_length=25)),
                ('company_email', models.EmailField(default='DEFAULT EMAIL', max_length=100)),
                ('company_location', models.CharField(default='DEFAULT LOC', max_length=25)),
                ('company_country', django_countries.fields.CountryField(default='US', max_length=2)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='files/users/user.username/%Y_%m_%d/')),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='files',
            field=models.ManyToManyField(to='registration.UserFiles'),
        ),
    ]
