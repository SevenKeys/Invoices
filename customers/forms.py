from django import forms
from .models import Customer, CustomerGroup



class CustomerForm(forms.ModelForm):
	name = forms.CharField(label='Client name')
	all_groups = CustomerGroup.objects.all()
	groups = forms.ModelMultipleChoiceField(queryset=all_groups, 
								   required=False)

	class Meta:
		model = Customer
		fields = ['name','status','groups','comment','language',
				  'client_type','discount_percent','company_segment']

	def __init__(self,*args,**kwargs):
		super(CustomerForm, self).__init__(*args, **kwargs)
		try:
			name = self.initial['name']
			customer = Customer.objects.get(name=name)
			self.fields['groups'].initial = CustomerGroup.objects.filter(
											  customers=customer)
		except KeyError:
			pass


class CustomerGroupForm(forms.ModelForm):
	name = forms.CharField(label='Client group name')

	class Meta:
		model = CustomerGroup
		fields = ['name','parent','category']

