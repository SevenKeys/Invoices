# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('phone_number', models.CharField(validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$', message="Phone number must be entered in the format: '+999999999'.Up to 15 digits allowed.")], max_length=16, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('street', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=60)),
                ('postcode', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=60)),
                ('website', models.CharField(max_length=150)),
            ],
        ),
    ]
