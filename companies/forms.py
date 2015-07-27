from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
	phone_number = forms.IntegerField()
	email = forms.EmailField()
	street = forms.CharField()
	city = forms.CharField()
	postcode = forms.IntegerField()
	country = forms.CharField()
	website = forms.CharField()
	phone_number = forms.IntegerField()
	user_name = forms.CharField()

	class Meta:
		model = Company
		fields = ['user_name', 'name', 'phone_number', 'email', 'street', 
				  'city', 'postcode','country','website','reg_code']