# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20150805_0825'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerdetails',
            old_name='discount_precent',
            new_name='discount_percent',
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='language',
            field=models.CharField(null=True, blank=True, max_length=25),
        ),
    ]
