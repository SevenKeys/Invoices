# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('created', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(null=True, to='companies.Company', blank=True)),
                ('contact', models.ForeignKey(to='contacts.Contact', null=True)),
            ],
        ),
    ]
