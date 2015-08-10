from django.contrib import admin

from .models import Customer
# from .models import CustomerDetails
from .models import CustomerGroup


admin.site.register(Customer)
# admin.site.register(CustomerDetails)
admin.site.register(CustomerGroup)
# Register your models here.
