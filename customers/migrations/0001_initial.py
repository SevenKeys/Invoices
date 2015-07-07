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
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('created', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(to='companies.Company')),
                ('contact', models.ForeignKey(to='contacts.Contact', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('field_name', models.CharField(max_length=100)),
                ('field_value', models.CharField(max_length=100)),
                ('customer', models.ForeignKey(to='customers.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('company', models.ForeignKey(to='companies.Company')),
                ('customers', models.ManyToManyField(to='customers.Customer')),
            ],
        ),
    ]
