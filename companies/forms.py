from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
	phone_number = forms.IntegerField()
	email = forms.EmailField()
	street = forms.CharField()
	postcode = forms.IntegerField()
	country = forms.CharField()
	website = forms.CharField()
	phone_number = forms.IntegerField()

	class Meta:
		model = Company
		fields = ['name', 'phone_number','email','street',
				'postcode','country','website','reg_code']