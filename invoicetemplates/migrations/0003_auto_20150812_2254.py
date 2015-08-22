# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20150808_0604'),
        ('invoicetemplates', '0002_archetype_archetypefield'),
    ]

    operations = [
        migrations.AddField(
            model_name='archetype',
            name='company',
            field=models.ForeignKey(to='companies.Company', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='template',
            name='archetype',
            field=models.ForeignKey(to='invoicetemplates.Archetype', null=True, blank=True),
        ),
    ]
