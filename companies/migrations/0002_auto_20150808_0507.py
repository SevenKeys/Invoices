# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='credit_status',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='office_number',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='segment',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
