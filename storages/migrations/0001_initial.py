# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(unique=True, max_length=25)),
                ('code', models.CharField(unique=True, max_length=50)),
                ('description', models.TextField()),
                ('max_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StorageGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(unique=True, max_length=25)),
            ],
        ),
        migrations.AddField(
            model_name='storage',
            name='group',
            field=models.ForeignKey(default='', blank=True, to='storages.StorageGroup'),
        ),
    ]
