from django import forms
from .models import *

class InvoiceForm(forms.Form):
	model = Invoice
	fields = ['title','companyTo']
