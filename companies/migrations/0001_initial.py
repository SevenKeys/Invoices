# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('reg_code', models.CharField(max_length=30)),
                ('contact', models.ForeignKey(null=True, to='contacts.Contact', blank=True)),
            ],
        ),
    ]
