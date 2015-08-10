# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20150805_0825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='group',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default='service', max_length=25),
        ),
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(blank=True, null=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='product',
            name='tax',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='units_of_measure',
            field=models.CharField(default='unit1', max_length=25),
        ),
    ]
