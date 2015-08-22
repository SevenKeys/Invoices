# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20150813_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tax',
            field=models.ForeignKey(default=0, to='products.Tax'),
        ),
    ]
