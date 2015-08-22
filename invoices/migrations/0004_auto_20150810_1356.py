# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
        ('invoices', '0003_auto_20150727_2156'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('default', models.BooleanField(default=False)),
                ('removable', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=40)),
                ('size_x', models.IntegerField()),
                ('size_y', models.IntegerField()),
                ('content', models.CharField(default='', max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(to='companies.Company', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TemplateComponentInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('reference', models.CharField(default='', max_length=200)),
                ('position_x', models.IntegerField()),
                ('position_y', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('component', models.ForeignKey(to='invoices.TemplateComponent')),
            ],
        ),
        migrations.RemoveField(
            model_name='invoicetemplatecomponent',
            name='component',
        ),
        migrations.RemoveField(
            model_name='invoicetemplatecomponent',
            name='invoiceTemplate',
        ),
        migrations.AddField(
            model_name='invoicetemplate',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='invoicetemplate',
            name='description',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='invoicecomponent',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='invoiceproduct',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='invoicetemplate',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='InvoiceTemplateComponent',
        ),
        migrations.AddField(
            model_name='templatecomponentinstance',
            name='template',
            field=models.ForeignKey(to='invoices.InvoiceTemplate', related_name='component_instances'),
        ),
    ]
