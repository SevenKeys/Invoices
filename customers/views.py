from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator
from django.core import serializers
from .models import Customer, CustomerGroup, CustomerCategory
from .models import Language, ClientType
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



class AddCustomer(CreateView, CompanyMixin):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/add_edit_customer.html'
    success_url = '/customers/success/'


    def form_valid(self, form):
        new_customer = form.save(commit=False)
        new_customer.company = self.get_company()
        # group = self.request.POST['group']
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


class SuccessCustomer(TemplateView):
    template_name = 'customers/add_customer_success.html'


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
    success_url = '/customers/success/'

    def get_context_data(self,**kwargs):
        context = super(UpdateCustomer, self).get_context_data(**kwargs)
        context['edit'] = True
        return context

    def form_valid(self, form):
        new_customer = form.save(commit=False)
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
    pk_url_kwarg = 'customer_group_id'

    def get_context_data(self,**kwargs):
        context = super(CustomerGroupDetail, self).get_context_data(**kwargs)
        try:
            company = self.get_company()
        except (Company.DoesNotExist, UserProfile.DoesNotExist):
            company = False
        context['company'] = company
        return context


class CustomerGroupList(ListView, CompanyMixin, LoginRequiredMixin):
    model = CustomerGroup
    template_name = 'customers/customer_groups/customer_group_list.html'
    context_object_name = 'customer_group_list'

    def get_context_data(self,**kwargs):
        context = super(CustomerGroupList, self).get_context_data(**kwargs)
        try:
            company = self.get_company()
        except (Company.DoesNotExist, UserProfile.DoesNotExist):
            company = False
        context['company'] = company
        return context

    def get_queryset(self):
        try:
            queryset = CustomerGroup.objects.order_by('name')
        except:
            queryset = False
        return queryset


class AddCustomerGroup(CreateView, CompanyMixin):
    model = CustomerGroup
    form_class = CustomerGroupForm
    template_name = 'customers/customer_groups/add_edit_customer_group.html'
    success_url = '/customers/success_group/'

    def get_context_data(self,**kwargs):
        context = super(AddCustomerGroup,self).get_context_data(**kwargs)
        context['company'] = self.get_company()
        return context

    def form_valid(self, form):
        customer_group = form.save(commit=False)
        customer_group.company = self.get_company()
        customer_group.save()
        return super(AddCustomerGroup,self).form_valid(form)


class SuccessCustomerGroup(TemplateView):
    template_name = '/customers/customer_groups/add_group_success.html'


class UpdateCustomerGroup(UpdateView, CompanyMixin):
    model = CustomerGroup
    form_class = CustomerGroupForm
    template_name = 'customers/customer_groups/add_edit_customer_group.html'
    pk_url_kwarg = 'customer_group_id'
    success_url = '/customers/success_group/'

    def get_context_data(self,**kwargs):
        context = super(UpdateCustomerGroup, self).get_context_data(**kwargs)
        context['edit'] = True
        context['company'] = self.get_company()
        return context


class DeleteCustomerGroup(DeleteView):
    model = CustomerGroup
    template_name = 'customers/delete_group.html'
    pk_url_kwarg = 'customer_group_id'
    success_url = reverse_lazy('customers')


# JS-GRID
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
        return HttpResponse(serializers.serialize("json", [q for q in results.page(1).object_list],
                                                  use_natural_foreign_keys=True),
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
        return HttpResponse(serializers.serialize("json", [q for q in results.page(1).object_list],
                                                  use_natural_foreign_keys=True),
                            content_type='application/json')


class CustomerListsJson(LoginRequiredMixin, ListView):
    def GetLanguageJson(self):
        try:
            name_filter = self.GET.get('name')
            id_filter = self.GET.get('id')
            queryset = Language.objects.all()
            if name_filter:
                queryset = queryset.filter(name__contains=name_filter)
            if id_filter != '0':
                queryset = queryset.filter(id=int(id_filter))
        except BaseException as exc:
            queryset = []
        results = Paginator(queryset.order_by('name'), 20)
        return HttpResponse(serializers.serialize("json", [q for q in results.page(1).object_list]),
                            content_type='application/json')
                            
    def GetTypeJson(self):
        try:
            name_filter = self.GET.get('name')
            id_filter = self.GET.get('id')
            queryset = ClientType.objects.all()
            if name_filter:
                queryset = queryset.filter(name__contains=name_filter)
            if id_filter != '0':
                queryset = queryset.filter(id=int(id_filter))
        except BaseException as exc:
            queryset = []
        results = Paginator(queryset.order_by('name'), 20)
        return HttpResponse(serializers.serialize("json", [q for q in results.page(1).object_list]),
                            content_type='application/json')
                            
    def GetCategoryJson(self):
        try:
            name_filter = self.GET.get('name')
            id_filter = self.GET.get('id')
            queryset = CustomerCategory.objects.all()
            if name_filter:
                queryset = queryset.filter(name__contains=name_filter)
            if id_filter != '0':
                queryset = queryset.filter(id=int(id_filter))
        except BaseException as exc:
            queryset = []
        results = Paginator(queryset.order_by('name'), 20)
        return HttpResponse(serializers.serialize("json", [q for q in results.page(1).object_list]),
                            content_type='application/json')
                            
                            
# CRUD for Language
class LanguageListView(ListView, CompanyMixin, LoginRequiredMixin):
    model = Language
    template_name = 'customers/languages/language_list.html'

    def get_context_data(self,**kwargs):
        context = super(LanguageListView, self).get_context_data(**kwargs)
        try:
            company = self.get_company()
        except (Company.DoesNotExist, UserProfile.DoesNotExist):
            company = False
        context['company'] = company
        return context


class LanguageAddView(CreateView):
    model = Language
    fields = ['name']
    template_name = 'customers/languages/add_edit_language.html'
    success_url = '/customers/success_language/'


class SuccessLanguage(TemplateView):
    template_name = 'customers/languages/success_language.html'


class LanguageDeleteView(DeleteView):
    model = Language
    template_name = 'customers/languages/language_list.html'
    pk_url_kwarg = 'language_id'
    success_url = '/customers/languages/'


class LanguageEditView(UpdateView):
    model = Language
    fields = ['name']
    template_name = 'customers/languages/add_edit_language.html'
    pk_url_kwarg = 'language_id'
    success_url = '/customers/success_language/'
    
    def get_context_data(self, **kwargs):
        context = super(LanguageEditView, self).get_context_data(**kwargs)
        context['edit'] = True
        return context


# CRUD for ClientType
class ClientTypeListView(ListView, CompanyMixin, LoginRequiredMixin):
    model = ClientType
    template_name = 'customers/client_types/client_type_list.html'

    def get_context_data(self,**kwargs):
        context = super(ClientTypeListView, self).get_context_data(**kwargs)
        try:
            company = self.get_company()
        except (Company.DoesNotExist, UserProfile.DoesNotExist):
            company = False
        context['company'] = company
        return context


class ClientTypeAddView(CreateView):
    model = ClientType
    fields = ['name']
    template_name = 'customers/client_types/add_edit_type.html'
    success_url = '/customers/success_type/'


class SuccessType(TemplateView):
    template_name = 'customers/client_types/success_type.html'
    
    
class ClientTypeDeleteView(DeleteView):
    model = ClientType
    template_name = 'customers/client_types/client_type_list.html'
    pk_url_kwarg = 'client_type_id'
    success_url = '/customers/success_type/'


class ClientTypeEditView(UpdateView):
    model = ClientType
    fields = ['name']
    template_name = 'customers/client_types/add_edit_type.html'
    pk_url_kwarg = 'client_type_id'
    success_url = '/customers/success_type/'
    
    def get_context_data(self, **kwargs):
        context = super(ClientTypeEditView, self).get_context_data(**kwargs)
        context['edit'] = True
        return context


# CRUD for customer categories
class CustCatListView(ListView, CompanyMixin, LoginRequiredMixin):
    model = CustomerCategory
    template_name = 'customers/customer_categories/cust_cat_list.html'

    def get_context_data(self,**kwargs):
        context = super(CustCatListView, self).get_context_data(**kwargs)
        try:
            company = self.get_company()
        except (Company.DoesNotExist, UserProfile.DoesNotExist):
            company = False
        context['company'] = company
        return context


class CustCatAddView(CreateView):
    model = CustomerCategory
    fields = ['name']
    template_name = 'customers/customer_categories/add_edit_cust_cat.html'
    success_url = '/customers/success_cust_cat/'


class SuccessCustCat(TemplateView):
    template_name = 'customers/customer_categories/success_cust_cat.html'


class CustCatDeleteView(DeleteView):
    model = CustomerCategory
    template_name = 'customers/customer_categories/cust_cat_list.html'
    pk_url_kwarg = 'cust_cat_id'
    success_url = '/customers/customer_categories/'


class CustCatEditView(UpdateView):
    model = CustomerCategory
    fields = ['name']
    template_name = 'customers/customer_categories/add_edit_cust_cat.html'
    pk_url_kwarg = 'cust_cat_id'
    success_url = '/customers/success_cust_cat/'
    
    def get_context_data(self, **kwargs):
        context = super(CustCatEditView, self).get_context_data(**kwargs)
        context['edit'] = True
        return context
