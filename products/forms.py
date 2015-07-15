from django import forms
from .models import Product, ProductGroup
from companies.models import Company

class ProductForm(forms.ModelForm):
	# Add extra field to see list of groups
	groups = forms.ModelMultipleChoiceField(queryset=ProductGroup.objects.all())

	class Meta:
		model = Product
		fields = ['company', 'name','groups']


	def save(self):
		product = super(ProductForm,self).save()
		groups = ProductGroup.objects.all()
		for group in groups:
			group.products.add(product)
			group.save()
		return product
	