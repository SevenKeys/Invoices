# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20150813_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='product',
            field=models.OneToOneField(null=True, blank=True, to='products.Product'),
        ),
        migrations.AlterField(
            model_name='currency',
            name='product',
            field=models.OneToOneField(null=True, blank=True, to='products.Product'),
        ),
        migrations.AlterField(
            model_name='tax',
            name='product',
            field=models.OneToOneField(null=True, blank=True, to='products.Product', related_name='product'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='product',
            field=models.OneToOneField(null=True, blank=True, to='products.Product'),
        ),
    ]
