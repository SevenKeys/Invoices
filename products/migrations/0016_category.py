# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20150819_1003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=True)),
                ('name', models.CharField(max_length=50)),
                ('product', models.ForeignKey(related_name='product', to='products.Product', blank=True, null=True)),
            ],
        ),
    ]
