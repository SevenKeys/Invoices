from django import forms
from .models import Customer, CustomerGroup


class CustomerForm(forms.ModelForm):
    languages = (('english', 'English'),
                 ('spanish', 'Spanish'),
                 ('russian', 'Russian'))
    types = (('retail', 'retail'),
             ('wholesale', 'wholesale'),
             ('dealer', 'dealer'))
    name = forms.CharField(label='Client name')
    language = forms.ChoiceField(choices=languages, required=False)
    client_type = forms.ChoiceField(choices=types, required=False)

    class Meta:
        model = Customer
        fields = ['name', 'status', 'comment', 'language',
                  'client_type', 'discount_percent']


class CustomerGroupForm(forms.ModelForm):
    name = forms.CharField(label='Client group name')

    class Meta:
        model = CustomerGroup
        fields = ['name', 'customers', 'parent', 'category']
