from django import forms
from .models import Product, ProductGroup, Currency, Category, Unit, Tax


class ProductForm(forms.ModelForm):
    cur = [((x.name),(x)) for x in Currency.objects.all()]
    categories = [((x.name),(x)) for x in Category.objects.all()]
    units = [((x.name),(x)) for x in Unit.objects.all()]
    taxes = [((x.value),(x)) for x in Tax.objects.all()]
    name = forms.CharField(label='Product name')
    currency = forms.ChoiceField(choices=cur,required=False)
    category = forms.ChoiceField(choices=categories)
    units_of_measure = forms.ChoiceField(choices=units)
    tax = forms.ChoiceField(choices=taxes)

    class Meta:
        model = Product
        fields = ['name', 'code', 'price', 'description', 'currency',
                  'category', 'stock', 'group', 'units_of_measure', 'tax', 'price_with_tax']


class ProductGroupForm(forms.ModelForm):
    categs = (
        ('categ1', 'category1'),
        ('categ2', 'category2'),
        ('categ3', 'category3'))
    category = forms.ChoiceField(choices=categs)

    class Meta:
        model = ProductGroup
        fields = ['name', 'parent', 'description', 'category']
