from django import forms
from .models import Customer, CustomerDetails, CustomerGroup



class CustomerForm(forms.ModelForm):
	name = forms.CharField(label='Client name')

	class Meta:
		model = Customer
		fields = ['name']


class CustomerGroupForm(forms.ModelForm):
	name = forms.CharField(label='Client group name')

	class Meta:
		model = CustomerGroup
		fields = ['name','customers']

class CustomerDetailForm(forms.ModelForm):

	class Meta:
		model = CustomerDetails
		fields = ['field_name', 'field_value']
