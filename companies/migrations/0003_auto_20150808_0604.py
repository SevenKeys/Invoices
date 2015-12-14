# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20150808_0507'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanySegment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.RemoveField(
            model_name='company',
            name='segment',
        ),
        migrations.AddField(
            model_name='companysegment',
            name='company',
            field=models.ForeignKey(to='companies.Company'),
        ),
    ]
