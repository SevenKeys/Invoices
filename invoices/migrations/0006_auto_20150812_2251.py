# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0005_templatecomponent_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoicetemplate',
            name='company',
        ),
        migrations.RemoveField(
            model_name='templatecomponent',
            name='company',
        ),
        migrations.RemoveField(
            model_name='templatecomponentinstance',
            name='component',
        ),
        migrations.RemoveField(
            model_name='templatecomponentinstance',
            name='template',
        ),
        migrations.DeleteModel(
            name='InvoiceTemplate',
        ),
        migrations.DeleteModel(
            name='TemplateComponent',
        ),
        migrations.DeleteModel(
            name='TemplateComponentInstance',
        ),
    ]
