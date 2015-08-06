# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerdetails',
            name='field_name',
        ),
        migrations.RemoveField(
            model_name='customerdetails',
            name='field_value',
        ),
        migrations.AddField(
            model_name='customerdetails',
            name='client_type',
            field=models.CharField(max_length=25, choices=[('retail', 'retail'), ('wholesale', 'wholesale'), ('dealer', 'dealer')], null=True, blank=True),
        ),
        migrations.AddField(
            model_name='customerdetails',
            name='comment',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='customerdetails',
            name='discount_precent',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='customerdetails',
            name='language',
            field=models.CharField(max_length=25, choices=[('english', 'English'), ('spanish', 'Spanish'), ('russian', 'Russian')], null=True, blank=True),
        ),
        migrations.AddField(
            model_name='customerdetails',
            name='status',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='customergroup',
            name='category',
            field=models.CharField(max_length=100, choices=[('cat1', 'category1'), ('cat2', 'category2'), ('cat3', 'category3')], null=True, blank=True),
        ),
        migrations.AddField(
            model_name='customergroup',
            name='parent',
            field=models.ManyToManyField(to='customers.CustomerGroup', default='client_group', blank=True),
        ),
    ]
