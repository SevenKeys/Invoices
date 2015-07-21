from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.http import HttpResponse
from .models import Customer, CustomerDetails, CustomerGroup
from .forms import CustomerForm, CustomerDetailForm, CustomerGroupForm
# from contacts.models import Contact
from users.models import User
from users.permissions import LoginRequiredMixin


# CRUD for Customer
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



# CRUD for CustomerGroup
class CustomerGroupDetail(ListView):
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


class AddCustomerGroup(CreateView):
	model = CustomerGroup
	form_class = CustomerGroupForm
	template_name = 'customers/edit_customer_group.html'
	success_url = '/customers/all/'

	def form_invalid(self,form):
		return HttpResponse('form is invalid')

	def get_context_data(self,**kwargs):
		context = super(AddCustomerGroup,self).get_context_data(**kwargs)
		user = self.request.user
		company = user.userprofile.company
		context['company'] = company
		return context

	def form_valid(self, form):
		customer_group = form.save(commit=False)
		user = self.request.user
		customer_group.company = user.userprofile.company
		customer_group.save()
		return super(AddCustomerGroup,self).form_valid(form)


class UpdateCustomerGroup(UpdateView):
	model = Customer
	form_class = CustomerForm
	template_name = 'customers/edit_customer.html'
	pk_url_kwarg = 'customer_id'
	success_url = '/customers/all/'


class DeleteCustomerGroup(DeleteView):
	model = Customer
	form_class = CustomerForm
	template_name = 'customers/delete_customer.html'
	pk_url_kwarg = 'customer_id'
	success_url = '/customers/all/'


# CRUD for CustomerDetails
class CustomerDetail(DetailView):
	model = Customer
	template_name = 'customers/customer_details.html'
	pk_url_kwarg = 'customer_id'


class AddCustomerDetail(CreateView):
	model = Customer
	form_class = CustomerDetailForm
	template_name = 'customers/edit_customer_detail.html'
	success_url = '/customers/all/'
	pk_url_kwarg = 'customer_id'

	def form_invalid(self,form):
		return HttpResponse('form is invalid')

	def form_valid(self, form):
		customer_detail = form.save(commit=False)
		customer = get_object_or_404(Customer,pk=self.kwargs[self.pk_url_kwarg])
		customer_detail.customer = customer
		customer_detail.save()
		return super(AddCustomerDetail,self).form_valid(form)


class UpdateCustomerDetail(UpdateView):
	model = CustomerDetails
	form_class = CustomerDetailForm
	template_name = 'customers/edit_customer_detail.html'
	pk_url_kwarg = 'detail_id'
	success_url = '/customers/all/'



class DeleteCustomerDetail(DeleteView):
	model = CustomerDetails
	form_class = CustomerDetailForm
	template_name = 'customers/delete_customer_detail.html'
	pk_url_kwarg = 'detail_id'
	success_url = '/customers/all/'