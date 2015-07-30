# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='city',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='contact',
            name='postcode',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='contact',
            name='street',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='website',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
