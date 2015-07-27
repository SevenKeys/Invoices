# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150725_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(blank=True, null=True, max_length=120),
        ),
    ]
