# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import django.core.validators
import django_countries.fields
import phonenumber_field.modelfields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('username', models.CharField(verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], unique=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, error_messages={'unique': 'A user with that username already exists.'})),
                ('first_name', models.CharField(verbose_name='first name', blank=True, max_length=30)),
                ('last_name', models.CharField(verbose_name='last name', blank=True, max_length=30)),
                ('email', models.EmailField(verbose_name='email address', blank=True, max_length=254)),
                ('is_staff', models.BooleanField(verbose_name='staff status', help_text='Designates whether the user can log into this admin site.', default=False)),
                ('is_active', models.BooleanField(verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('user_type', models.CharField(default='INV_USR', max_length=7, choices=[('CMP_USR', 'Company'), ('INV_USR', 'Investor')])),
                ('admin_status', models.BooleanField(default=0)),
                ('groups', models.ManyToManyField(verbose_name='groups', related_name='user_set', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', to='auth.Group', blank=True, related_query_name='user')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', related_name='user_set', help_text='Specific permissions for this user.', to='auth.Permission', blank=True, related_query_name='user')),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=150)),
                ('company_name', models.CharField(max_length=50)),
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
    ]
