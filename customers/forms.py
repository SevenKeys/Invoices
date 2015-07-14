from django import forms
from .models import Customer, CustomerDetails, CustomerGroup

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ['company','name','contact']
