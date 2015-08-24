# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0004_auto_20150810_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='templatecomponent',
            name='type',
            field=models.CharField(default='custom', max_length=10),
        ),
    ]
