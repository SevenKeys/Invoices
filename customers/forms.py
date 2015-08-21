from django import forms
from .models import Customer, CustomerGroup



class CustomerForm(forms.ModelForm):
	groups = [((x),(x.name)) for x in CustomerGroup.objects.all()]
	name = forms.CharField(label='Client name')
	group = forms.ChoiceField(choices=groups,required=False)

	class Meta:
		model = Customer
		fields = ['name','status','group','comment','language',
				  'client_type','discount_percent','company_segment']


class CustomerGroupForm(forms.ModelForm):
	categories = (
		    ('cat1','category1'),
		    ('cat2','category2'),
		    ('cat3','category3'))
	name = forms.CharField(label='Client group name')
	category = forms.ChoiceField(choices=categories,required=False)

	class Meta:
		model = CustomerGroup
		fields = ['name','customers','parent','category']

