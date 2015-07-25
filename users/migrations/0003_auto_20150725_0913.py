# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150717_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='created',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
    ]
