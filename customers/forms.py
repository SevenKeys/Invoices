from django import forms
from .models import Customer, CustomerGroup



class CustomerForm(forms.ModelForm):
	languages = (('english','English'),
			     ('spanish','Spanish'),
			     ('russian','Russian'))
	types = (('retail','retail'),
		     ('wholesale','wholesale'),
		     ('dealer','dealer'))
	groups = [((x),(x.name)) for x in CustomerGroup.objects.all()]
	name = forms.CharField(label='Client name')
	# status = forms.NullBooleanField(required=False)
	# comment = forms.CharField(widget=forms.Textarea,required=False)
	language = forms.ChoiceField(choices=languages,required=False)
	client_type = forms.ChoiceField(choices=types,required=False)
	# discount_percent = forms.FloatField(required=False)
	group = forms.ChoiceField(choices=groups,required=False)


	class Meta:
		model = Customer
		fields = ['name','status','group','comment','language',
				  'client_type','discount_percent']


class CustomerGroupForm(forms.ModelForm):
	name = forms.CharField(label='Client group name')

	class Meta:
		model = CustomerGroup
		fields = ['name','customers','parent','category']

# class CustomerDetailForm(forms.ModelForm):

# 	class Meta:
# 		model = CustomerDetails
# 		fields = ['status','customer','comment','language',
# 				  'client_type','discount_precent']
