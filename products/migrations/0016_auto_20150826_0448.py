# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20150822_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(to='products.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.ForeignKey(to='products.Unit'),
        ),
    ]
