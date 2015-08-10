# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20150806_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.ForeignKey(default='', blank=True, to='products.ProductGroup'),
        ),
    ]
