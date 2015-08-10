# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20150806_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.ForeignKey(null=True, blank=True, to='products.ProductGroup'),
        ),
    ]
