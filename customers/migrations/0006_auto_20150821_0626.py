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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerManager',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=25)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='client_type',
            field=models.ForeignKey(blank=True, null=True, to='customers.ClientType'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='language',
            field=models.ForeignKey(blank=True, null=True, to='customers.Language'),
        ),
        migrations.AlterField(
            model_name='customergroup',
            name='category',
            field=models.ForeignKey(blank=True, null=True, to='customers.CustomerCategory'),
        ),
        migrations.AlterField(
            model_name='customergroup',
            name='parent',
            field=models.ManyToManyField(blank=True, to='customers.CustomerGroup', default=''),
        ),
    ]
