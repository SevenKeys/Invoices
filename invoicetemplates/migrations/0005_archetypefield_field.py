# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoicetemplates', '0004_auto_20150813_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='archetypefield',
            name='field',
            field=models.CharField(max_length=50, default='field'),
        ),
    ]
