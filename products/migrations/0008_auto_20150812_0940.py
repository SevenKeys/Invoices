# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20150806_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='product',
            name='units_of_measure',
        ),
        migrations.AddField(
            model_name='unit',
            name='product',
            field=models.ForeignKey(to='products.Product', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='currency',
            name='product',
            field=models.ForeignKey(to='products.Product', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='product',
            field=models.ForeignKey(to='products.Product', null=True, blank=True),
        ),
    ]
