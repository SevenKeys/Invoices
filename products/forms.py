from django import forms
from .models import Product, ProductGroup
from companies.models import Company

class ProductForm(forms.ModelForm):
	cur = (
		('usd','USD'),
		('eur','EUR'),
		('rub','RUB'))
	categories = (
		('service','service'),
		('item','item'))
	units = (
		('unit1','unit1'),
		('unit2','unit2'),
		('unit3','unit3'))
	taxes = (
		(2,'2'),
		(4,'4'),
		(6,'6'))
	# groups = ProductGroup.objects.all()
	name = forms.CharField(label='Product name')
	currency = forms.ChoiceField(choices=cur)
	category = forms.ChoiceField(choices=categories)
	units_of_measure = forms.ChoiceField(choices=units)
	tax = forms.ChoiceField(choices=taxes)
	# group = forms.ChoiceField(choices=groups,required=False)

	class Meta:
		model = Product
		fields = ['name','code','price','description','currency',
		'category','stock','group','units_of_measure','tax','price_with_tax']


class ProductGroupForm(forms.ModelForm):
	categs = (
		('categ1','category1'),
		('categ2','category2'),
		('categ3','category3'))
	class Meta:
		model = ProductGroup
		fields = ['name']

	
	