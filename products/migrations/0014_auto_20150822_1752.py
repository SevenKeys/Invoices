# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20150813_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductGroupCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='productgroup',
            name='category',
        ),
        migrations.RemoveField(
            model_name='productgroup',
            name='parent',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='currency',
            name='name',
            field=models.CharField(unique=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.ForeignKey(null=True, to='products.Currency', blank=True),
        ),
        migrations.AlterField(
            model_name='tax',
            name='value',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
