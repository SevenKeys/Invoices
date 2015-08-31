# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20150826_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.ForeignKey(default='', blank=True, to='products.Currency'),
        ),
    ]
