# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoicetemplates', '0005_archetypefield_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='content',
            field=models.CharField(default='', max_length=3000),
        ),
    ]
