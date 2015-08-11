from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator
from django.core import serializers
from .models import Customer, CustomerGroup
from .forms import CustomerForm, CustomerGroupForm
from companies.models import Company
from users.models import UserProfile
from users.permissions import LoginRequiredMixin
from companies.views import CompanyMixin, NavMenuView
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
    #   context = super(CustomerList, self).get_context_data()
    #   try:
    #       company = self.get_company()
    #   except UserProfile.DoesNotExist:
    #       company = False
    #   context['company'] = company
    #   return context



class AddCustomer(CreateView, CompanyMixin):
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

    def get_context_data(self,**kwargs):
        context = super(AddCustomer, self).get_context_data(**kwargs)
        try:
            company = self.get_company()
        except (UserProfile.DoesNotExist, Company.DoesNotExist):
            company = False
        context['company'] = company
        return context


class CustomerDetail(DetailView,CompanyMixin):
    model = Customer
    template_name = 'customers/customer_details.html'
    pk_url_kwarg = 'customer_id'

    def get_context_data(self,**kwargs):
        context = super(CustomerDetail, self).get_context_data(**kwargs)
        try:
            company = self.get_company()
        except (Company.DoesNotExist, UserProfile.DoesNotExist):
            company = False
        context['company'] = company
        return context


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
    pk_url_kwarg = 'customer_id'
    success_url = '/customers/all/'



# CRUD for CustomerGroup
class CustomerGroupDetail(DetailView, CompanyMixin):
    model = CustomerGroup
    template_name = 'customers/group_details.html'
    pk_url_kwarg = 'group_id'

    def get_context_data(self,**kwargs):
        context = super(CustomerGroupDetail, self).get_context_data(**kwargs)
        try:
            company = self.get_company()
        except (Company.DoesNotExist, UserProfile.DoesNotExist):
            company = False
        context['company'] = company
        return context



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



class CustomerListJson(LoginRequiredMixin, CompanyMixin, ListView):
    def GetCustomersJson(self):
        try:
            user = self.user
            company = user.userprofile.company
            segment_filter = self.GET.get('company_segment')
            type_filter = self.GET.get('client_type')
            status_filter = self.GET.get('status')
            name_filter = self.GET.get('name')
            queryset = Customer.objects.filter(company=company)
            if name_filter:
                queryset = queryset.filter(name__contains=name_filter)
            if status_filter:
                queryset = queryset.filter(status__contains=status_filter)
            if type_filter:
                queryset = queryset.filter(client_type__contains=type_filter)
            if segment_filter:
                queryset = queryset.filter(company_segment__contains=segment_filter)
        except BaseException as exc:
            queryset = []
        results = Paginator(queryset.order_by('name'), 20)
        return HttpResponse(serializers.serialize("json", [q for q in results.page(1).object_list]),
                            content_type='application/json')


class CustomerGroupListJson(LoginRequiredMixin, CompanyMixin, ListView):
    def GetCustomerGroupsJson(self):
        try:
            user = self.user
            company = user.userprofile.company
            category_filter = self.GET.get('category')
            parent_filter = self.GET.get('parent')
            name_filter = self.GET.get('name')
            queryset = CustomerGroup.objects.filter(company=company)
            if name_filter:
                queryset = queryset.filter(name__contains=name_filter)
            if category_filter:
                queryset = queryset.filter(category__contains=category_filter)
            if parent_filter:
                queryset = queryset.filter(parent__contains=parent_filter)
        except BaseException as exc:
            queryset = []
        results = Paginator(queryset.order_by('name'), 20)
        return HttpResponse(serializers.serialize("json", [q for q in results.page(1).object_list]),
                            content_type='application/json')