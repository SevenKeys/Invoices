# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20150808_0604'),
        ('customers', '0006_auto_20150822_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='client_type',
            field=models.ForeignKey(to='customers.ClientType', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='company_segment',
            field=models.ForeignKey(to='companies.CompanySegment', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='discount_percent',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='language',
            field=models.ForeignKey(to='customers.Language', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customergroup',
            name='category',
            field=models.ForeignKey(to='customers.CustomerCategory', blank=True, null=True),
        ),
    ]
