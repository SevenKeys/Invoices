# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20150806_0954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productgroup',
            name='products',
        ),
        migrations.AddField(
            model_name='product',
            name='group',
            field=models.ForeignKey(default='', to='products.ProductGroup', blank=True),
        ),
        migrations.AlterField(
            model_name='productgroup',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
