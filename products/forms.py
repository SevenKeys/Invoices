from django import forms
from .models import Product, ProductGroup, Currency, Category, Unit, Tax


class ProductForm(forms.ModelForm):
    name = forms.CharField(label='Product name')

    class Meta:
        model = Product
        fields = ['name', 'code', 'price', 'description', 'currency',
                  'category', 'stock', 'group', 'unit', 'tax', 'price_with_tax']


class ProductGroupForm(forms.ModelForm):
    categs = (
        ('categ1', 'category1'),
        ('categ2', 'category2'),
        ('categ3', 'category3'))
    category = forms.ChoiceField(choices=categs)

    class Meta:
        model = ProductGroup
        fields = ['name', 'parent', 'description', 'category']
