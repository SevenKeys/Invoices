# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20150828_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.ForeignKey(to='products.Unit', blank=True, null=True),
        ),
    ]
