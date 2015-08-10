# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20150730_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='street',
            field=models.CharField(max_length=200),
        ),
    ]
