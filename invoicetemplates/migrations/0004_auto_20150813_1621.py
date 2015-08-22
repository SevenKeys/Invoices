# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoicetemplates', '0003_auto_20150812_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchetypeElement',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('code', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='archetypefield',
            name='field',
        ),
        migrations.AddField(
            model_name='archetypefield',
            name='element',
            field=models.ForeignKey(to='invoicetemplates.ArchetypeElement', blank=True, null=True),
        ),
    ]
