from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from .models import Customer, CustomerGroup
from .forms import CustomerForm, CustomerGroupForm
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

	# def get_context_data(self):
	# 	context = super(CustomerList, self).get_context_data()
	# 	try:
	# 		company = self.get_company()
	# 	except UserProfile.DoesNotExist:
	# 		company = False
	# 	context['company'] = company
	# 	return context



class AddCustomer(CreateView, CompanyMixin, ContactMixin):
	model = Customer
	form_class = CustomerForm
	template_name = 'customers/add_edit_customer.html'
	success_url = '/customers/all/'


	def form_valid(self, form):
		new_customer = form.save(commit=False)
		new_customer.company = self.get_company()
		group = self.request.POST['group']
		new_customer.save()
		return super(AddCustomer, self).form_valid(form)


class CustomerDetail(DetailView):
	model = Customer
	template_name = 'customers/customer_details.html'
	pk_url_kwarg = 'customer_id'

	# def get_context_data(self,**kwargs):
	# 	context = super(CustomerDetail, self).get_context_data(**kwargs)
	# 	user = self.request.user.userprofile.name
	# 	context['user_name'] = user
	# 	return context


class UpdateCustomer(UpdateView):
	model = Customer
	form_class = CustomerForm
	template_name = 'customers/add_edit_customer.html'
	pk_url_kwarg = 'customer_id'
	success_url = '/customers/all/'

	def get_context_data(self,**kwargs):
		context = super(UpdateCustomer, self).get_context_data(**kwargs)
		context['edit'] = True
		return context

	def form_valid(self, form):
		new_customer = form.save(commit=False)
		name_group = self.request.POST['group']
		group = CustomerGroup.objects.get(name=name_group)
		group.customers.add(new_customer)
		group.save()
		new_customer.save()
		return super(UpdateCustomer, self).form_valid(form)


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
	template_name = 'customers/add_edit_customer_group.html'
	success_url = '/customers/all/'

	def get_context_data(self,**kwargs):
		context = super(AddCustomerGroup,self).get_context_data(**kwargs)
		context['company'] = self.get_company()
		return context

	def form_valid(self, form):
		customer_group = form.save(commit=False)
		customer_group.company = self.get_company()
		customer_group.save()
		return super(AddCustomerGroup,self).form_valid(form)


class UpdateCustomerGroup(UpdateView, CompanyMixin):
	model = CustomerGroup
	form_class = CustomerGroupForm
	template_name = 'customers/add_edit_customer_group.html'
	pk_url_kwarg = 'group_id'
	success_url = '/customers/all/'

	def get_context_data(self,**kwargs):
		context = super(UpdateCustomerGroup, self).get_context_data(**kwargs)
		context['edit'] = True
		context['company'] = self.get_company()
		return context


class DeleteCustomerGroup(DeleteView):
	model = CustomerGroup
	template_name = 'customers/delete_group.html'
	pk_url_kwarg = 'group_id'
	success_url = reverse_lazy('customers')



def searchCustAjax(request):
	if request.method == 'POST':
		search_text = request.POST['search_text']
	else:
		search_text = ''
	customers = Customer.objects.filter(name__icontains=search_text)
	context = {};
	context['customers'] = customers

	return render(request, 'customers/search_customers_results.html', context)