from django import forms
from .models import Customer, CustomerDetails, CustomerGroup

class CustomerForm(forms.ModelForm):

	class Meta:
		model = Customer
		fields = ['name','contact']


class CustomerGroupForm(forms.ModelForm):

	class Meta:
		model = CustomerGroup
		fields = ['name','customers']

class CustomerDetailForm(forms.ModelForm):

	class Meta:
		model = CustomerDetails
		fields = ['field_name', 'field_value']
