# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20150828_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.ForeignKey(to='products.Currency', null=True, default='', blank=True),
        ),
    ]
