# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=25, default='service', choices=[('service', 'service'), ('item', 'item')]),
        ),
        migrations.AddField(
            model_name='product',
            name='code',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='currency',
            field=models.CharField(max_length=25, choices=[('usd', 'USD'), ('eur', 'EUR'), ('rub', 'RUB')], null=True, blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='group',
            field=models.CharField(max_length=100, default='', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='product',
            name='price_with_tax',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='tax',
            field=models.IntegerField(default=2, choices=[(2, '2'), (4, '4'), (6, '6')]),
        ),
        migrations.AddField(
            model_name='product',
            name='units_of_measure',
            field=models.CharField(max_length=25, default='unit1', choices=[('unit1', 'unit1'), ('unit2', 'unit2'), ('unit3', 'unit3')]),
        ),
        migrations.AddField(
            model_name='productgroup',
            name='category',
            field=models.CharField(max_length=100, choices=[('categ1', 'category1'), ('categ2', 'category2'), ('categ3', 'category3')], null=True, blank=True),
        ),
        migrations.AddField(
            model_name='productgroup',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='productgroup',
            name='parent',
            field=models.ManyToManyField(to='products.ProductGroup', default='goods', blank=True),
        ),
    ]
