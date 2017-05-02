# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import django.core.validators
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('username', models.CharField(unique=True, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], verbose_name='username', error_messages={'unique': 'A user with that username already exists.'})),
                ('first_name', models.CharField(verbose_name='first name', blank=True, max_length=30)),
                ('last_name', models.CharField(verbose_name='last name', blank=True, max_length=30)),
                ('email', models.EmailField(verbose_name='email address', blank=True, max_length=254)),
                ('is_staff', models.BooleanField(verbose_name='staff status', help_text='Designates whether the user can log into this admin site.', default=False)),
                ('is_active', models.BooleanField(verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('user_type', models.CharField(max_length=7, default='INV_USR', choices=[('CMP_USR', 'Company'), ('INV_USR', 'Investor')])),
                ('admin_status', models.BooleanField(default=0)),
                ('public_key', models.CharField(max_length=1000, null=True)),
                ('groups', models.ManyToManyField(to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', verbose_name='groups', related_query_name='user', blank=True)),
                ('user_permissions', models.ManyToManyField(to='auth.Permission', help_text='Specific permissions for this user.', related_name='user_set', verbose_name='user permissions', related_query_name='user', blank=True)),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('timestamp', models.DateTimeField(null=True)),
                ('enc_file_op', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=150, default='DEFAULT USERNAME')),
                ('company_name', models.CharField(max_length=50, default='DEFAULT COMPANY')),
                ('company_phone', models.CharField(max_length=11)),
                ('ceo', models.CharField(max_length=25, default='DEFAULT CEO')),
                ('company_email', models.EmailField(max_length=100, default='DEFAULT EMAIL')),
                ('company_location', models.CharField(max_length=25, default='DEFAULT LOC')),
                ('company_country', models.CharField(max_length=25, default='DEFAULT COUNTRY')),
                ('company_sector', models.CharField(max_length=25, default='DEFAULT SECTOR')),
                ('company_industry', models.CharField(max_length=25, default='DEFAULT INDUSTRY')),
                ('company_projects', models.CharField(max_length=25, default='DEFAULT PROJECT')),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('file', models.FileField(upload_to='files/users/user.username/%Y_%m_%d/')),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='files',
            field=models.ManyToManyField(to='registration.UserFiles', null=True),
        ),
    ]
