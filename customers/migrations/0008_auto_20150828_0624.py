# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0007_auto_20150822_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='client_type',
            field=models.ForeignKey(verbose_name='client type', blank=True, to='customers.ClientType', null=True),
        ),
    ]
