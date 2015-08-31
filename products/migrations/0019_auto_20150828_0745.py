# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_auto_20150828_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.ForeignKey(to='products.Currency', blank=True, null=True),
        ),
    ]
