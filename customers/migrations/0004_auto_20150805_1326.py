# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20150805_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerdetails',
            name='customer',
        ),
        migrations.AddField(
            model_name='customer',
            name='client_type',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='discount_percent',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='language',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='status',
            field=models.NullBooleanField(),
        ),
        migrations.DeleteModel(
            name='CustomerDetails',
        ),
    ]
