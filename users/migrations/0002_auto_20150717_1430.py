# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0001_initial'),
        ('companies', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('created', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(to='companies.Company', null=True, blank=True)),
                ('contact', models.ForeignKey(null=True, to='contacts.Contact')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='company',
        ),
        migrations.RemoveField(
            model_name='user',
            name='contact',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
