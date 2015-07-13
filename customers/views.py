# from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Customer, CustomerDetails, CustomerGroups
from contacts.models import Contact

# Create your views here.
class CustomerList(ListView):
	# model = Customer

	queryset = Customer.objects.all()
	context_objects_name = 'customer_list'
	template_name = 'customers/customer_list.html'

class CustomerDetail(DetailView):

	# queryset = CustomerDetails.objects.all()
	context_objects_name = 'customer_details'
	template_name = 'customers/customer_details.html'

	def get_object(self):
		return Customer.objects.get(pk=self.args[0])

