from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.http import HttpResponse
from .models import Customer, CustomerDetails, CustomerGroup
from .forms import CustomerForm
# from contacts.models import Contact
from users.models import User
from users.permissions import LoginRequiredMixin



class CustomerList(LoginRequiredMixin, ListView):
	context_objects_name = 'customer_list'
	template_name = 'customers/customer_list.html'

	def get_queryset(self):
		try:
			user = User.objects.get(username=self.request.user)
			if user:
				company = user.userprofile.company
				return Customer.objects.filter(company=company)
			else:
				return False
		except User.DoesNotExist:
			return False


class CustomerDetail(ListView):
	context_object_name = 'customer_details'
	template_name = 'customers/customer_details.html'
	pk_url_kwarg = 'customer_id'

	def get_queryset(self):
		self.customer = get_object_or_404(Customer,pk=self.kwargs[self.pk_url_kwarg])
		queryset = CustomerDetails.objects.filter(customer__name=self.customer)
		return queryset

	def get_context_data(self,**kwargs):
		context = super(CustomerDetail,self).get_context_data(**kwargs)
		context['customer_group'] = self.customer.customergroup_set.all()
		return context


class AddCustomer(CreateView):
	model = Customer
	form_class = CustomerForm
	template_name = 'customers/edit_customer.html'
	success_url = '/customers/all/'

	def form_invalid(self,form):
		return HttpResponse('form is invalid')


class UpdateCustomer(UpdateView):
	model = Customer
	form_class = CustomerForm
	template_name = 'customers/edit_customer.html'
	pk_url_kwarg = 'customer_id'
	success_url = '/customers/all/'


class DeleteCustomer(DeleteView):
	model = Customer
	form_class = CustomerForm
	template_name = 'customers/delete_customer.html'
	pk_url_kwarg = 'customer_id'
	success_url = '/customers/all/'
