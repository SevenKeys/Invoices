# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20150808_0604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('default', models.BooleanField(default=False)),
                ('removable', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=40)),
                ('size_x', models.IntegerField()),
                ('size_y', models.IntegerField()),
                ('type', models.CharField(max_length=10, default='custom')),
                ('content', models.CharField(max_length=1000, default='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(null=True, to='companies.Company', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ComponentInstance',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('reference', models.CharField(max_length=200, default='')),
                ('position_x', models.IntegerField()),
                ('position_y', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('component', models.ForeignKey(to='invoicetemplates.Component')),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=300, default='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('company', models.ForeignKey(to='companies.Company')),
            ],
        ),
        migrations.AddField(
            model_name='componentinstance',
            name='template',
            field=models.ForeignKey(to='invoicetemplates.Template', related_name='component_instances'),
        ),
    ]
