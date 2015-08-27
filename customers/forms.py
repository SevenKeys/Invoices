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
	name = forms.CharField(label='Client group name')

	class Meta:
		model = CustomerGroup
		fields = ['name','parent','category']

