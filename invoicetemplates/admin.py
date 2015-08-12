from .models import InvoiceTemplate, TemplateComponent, TemplateComponentInstance
from django.contrib import admin

admin.site.register(InvoiceTemplate)
admin.site.register(TemplateComponent)
admin.site.register(TemplateComponentInstance)
