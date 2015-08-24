# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_auto_20150808_0604'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='client_type',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='company_segment',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='discount_percent',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='language',
        ),
        migrations.RemoveField(
            model_name='customergroup',
            name='category',
        ),
        migrations.AlterField(
            model_name='customergroup',
            name='parent',
            field=models.ManyToManyField(to='customers.CustomerGroup', blank=True, default=''),
        ),
    ]
