# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20150822_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='productgroup',
            name='category',
            field=models.ForeignKey(null=True, blank=True, to='products.ProductGroupCategory'),
        ),
        migrations.AddField(
            model_name='productgroup',
            name='parent',
            field=models.ManyToManyField(default='', blank=True, to='products.ProductGroup'),
        ),
    ]
