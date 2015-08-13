# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20150813_1231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='product',
        ),
        migrations.RemoveField(
            model_name='currency',
            name='product',
        ),
        migrations.RemoveField(
            model_name='tax',
            name='product',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='', to='products.Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='currency',
            field=models.ForeignKey(default='', to='products.Currency'),
        ),
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.ForeignKey(default='', to='products.Unit'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tax',
            field=models.ForeignKey(default='', to='products.Tax'),
        ),
    ]
