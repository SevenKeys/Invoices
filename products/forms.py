from django import forms
from .models import Product, ProductGroup, Currency, Category, Unit, Tax


class ProductForm(forms.ModelForm):
    name = forms.CharField(label='Product name')

    class Meta:
        model = Product
        fields = ['name', 'code', 'price', 'description', 'currency',
                  'category', 'stock', 'group', 'unit', 'tax', 'price_with_tax']



class ProductGroupForm(forms.ModelForm):

    class Meta:
        model = ProductGroup
        fields = ['name', 'parent', 'description', 'category']
