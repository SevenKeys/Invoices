from django.contrib import admin

# Register your models here.

from .models import Company
from .models import Invoice
from .models import InvoiceComponent


admin.site.register(Company)
admin.site.register(Invoice)
admin.site.register(InvoiceComponent)


