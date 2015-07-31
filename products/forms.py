from django import forms
from .models import Product, ProductGroup
from companies.models import Company

class ProductForm(forms.ModelForm):
	name = forms.CharField(label='Product name')
	class Meta:
		model = Product
		fields = ['name']


class ProductGroupForm(forms.ModelForm):
	class Meta:
		model = ProductGroup
		fields = ['name','products']

	
	