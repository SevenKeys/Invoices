# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20150808_0604'),
        ('customers', '0004_auto_20150805_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='company_segment',
            field=models.ForeignKey(to='companies.CompanySegment', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='customergroup',
            name='category',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
    ]
