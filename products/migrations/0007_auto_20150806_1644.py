# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20150806_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.ForeignKey(null=True, to='products.ProductGroup', blank=True),
        ),
    ]
