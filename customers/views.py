from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from .models import Customer, CustomerDetails, CustomerGroup
from .forms import CustomerForm, CustomerDetailForm, CustomerGroupForm
# from contacts.models import Contact
from users.models import UserProfile
from users.permissions import LoginRequiredMixin
from companies.views import CompanyMixin
from contacts.views import ContactMixin


# CRUD for Customer
class CustomerList(LoginRequiredMixin, CompanyMixin, ListView):
	context_object_name = 'customer_list'
	template_name = 'customers/customer_list.html'

	def get_queryset(self):
		try:
			company = self.get_company()
			queryset = Customer.objects.filter(company=company).order_by('name')
		except:
			queryset = False
		return queryset

	def get_context_data(self):
		context = super(CustomerList, self).get_context_data()
		try:
			company = self.get_company()
		except UserProfile.DoesNotExist:
			company = False
		context['company'] = company
		return context



class AddCustomer(CreateView, CompanyMixin, ContactMixin):
	model = Customer
	form_class = CustomerForm
	template_name = 'customers/edit_customer.html'
	success_url = '/customers/all/'

	# def form_invalid(self,form):
	# 	return HttpResponse('form is invalid')

	def form_valid(self, form):
		new_customer = form.save(commit=False)
		new_customer.company = self.get_company()
		new_customer.contact = self.get_contact()
		new_customer.save()
		return super(AddCustomer, self).form_valid(form)


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
class CustomerGroupDetail(DetailView):
	model = CustomerGroup
	template_name = 'customers/group_details.html'
	pk_url_kwarg = 'group_id'

	# def get_queryset(self):
	# 	group = CustomerGroup.objects.get(pk=self.pk_url_kwarg)
	# 	queryset = group.customers.order_by('name')
	# 	return queryset



class AddCustomerGroup(CreateView, CompanyMixin):
	model = CustomerGroup
	form_class = CustomerGroupForm
	template_name = 'customers/edit_customer_group.html'
	success_url = '/customers/all/'

	# def form_invalid(self,form):
	# 	return HttpResponse('form is invalid')

	def get_context_data(self,**kwargs):
		context = super(AddCustomerGroup,self).get_context_data(**kwargs)
		context['company'] = self.get_company()
		return context

	def form_valid(self, form):
		customer_group = form.save(commit=False)
		customer_group.company = self.get_company()
		customer_group.save()
		return super(AddCustomerGroup,self).form_valid(form)


class UpdateCustomerGroup(UpdateView):
	model = CustomerGroup
	form_class = CustomerGroupForm
	template_name = 'customers/edit_customer_group.html'
	pk_url_kwarg = 'group_id'
	success_url = '/customers/all/'


class DeleteCustomerGroup(DeleteView):
	model = CustomerGroup
	template_name = 'customers/delete_group.html'
	pk_url_kwarg = 'group_id'
	success_url = reverse_lazy('customers')


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

	# def form_invalid(self,form):
	# 	return HttpResponse('form is invalid')

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


def searchCustAjax(request):
	if request.method == 'POST':
		search_text = request.POST['search_text']
	else:
		search_text = ''
	customers = Customer.objects.filter(name__icontains=search_text)
	context = {};
	context['customers'] = customers

	return render(request, 'customers/search_customers_results.html', context)