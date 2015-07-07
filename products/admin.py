from django.contrib import admin

from .models import Product
from .models import ProductGroup

admin.site.register(Product)
admin.site.register(ProductGroup)
