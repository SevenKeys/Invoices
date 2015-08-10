from django.contrib import admin

# Register your models here.

from .models import Company
from .models import Invoice
from .models import InvoiceTemplate
from .models import InvoiceComponent
from .models import TemplateComponent
from .models import TemplateComponentInstance

admin.site.register(Company)
admin.site.register(Invoice)
admin.site.register(InvoiceTemplate)
admin.site.register(InvoiceComponent)
admin.site.register(TemplateComponent)
admin.site.register(TemplateComponentInstance)

