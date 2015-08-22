# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_tax'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tax',
            name='name',
        ),
        migrations.AddField(
            model_name='tax',
            name='value',
            field=models.IntegerField(default=0),
        ),
    ]
