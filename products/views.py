from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.core import serializers
from companies.models import Company
from .models import Product, ProductGroup
from .models import Currency, Category, Unit, Tax
from users.models import UserProfile
from .forms import ProductForm, ProductGroupForm
from users.permissions import LoginRequiredMixin
from companies.views import CompanyMixin


# CRUD for Product app
class ProductList(LoginRequiredMixin, CompanyMixin, ListView):
    context_object_name = 'product_list'
    template_name = 'products/product_list.html'
    paginate_by = '10'

    def get_queryset(self):
        try:
            company = self.get_company()
            queryset = Product.objects.filter(company=company).order_by('name')
        except:
            queryset = False
        return queryset


class AddProduct(CreateView, CompanyMixin):
    model = Product
    form_class = ProductForm
    template_name = 'products/add_edit_product.html'
    success_url = '/products/all/'

    def form_valid(self, form):
        new_product = form.save(commit=False)
        new_product.company = self.get_company()
        new_product.save()
        return super(AddProduct,self).form_valid(form)

    def get_context_data(self,**kwargs):
        context = super(AddProduct, self).get_context_data(**kwargs)
        try:
            company = self.get_company()
        except (Company.DoesNotExist, UserProfile.DoesNotExist):
            company = False
        context['company'] = company
        context['add'] = True
        return context


class UpdateProduct(UpdateView, CompanyMixin):
    model = Product
    form_class = ProductForm
    template_name = 'products/add_edit_product.html'
    pk_url_kwarg = 'product_id'
    success_url = '/products/all/'

    def get_context_data(self,**kwargs):
        context = super(UpdateProduct, self).get_context_data(**kwargs)
        try:
            company = self.get_company()
        except (Company.DoesNotExist, UserProfile.DoesNotExist):
            company = False
        context['company'] = company
        context['add'] = False
        return context

    def form_valid(self, form):
        new_product = form.save(commit=False)
        new_product.save()
        return super(UpdateProduct,self).form_valid(form)


class DeleteProduct(DeleteView):
    model = Product
    form_class = ProductForm
    pk_url_kwarg = 'product_id'
    success_url = '/products/all/'


# CRUD for Product Group App
class ProductGroupList(LoginRequiredMixin, CompanyMixin, ListView):
    context_object_name = 'product_group_list'
    template_name = 'products/product_group_list.html'
    # paginate_by = '10'
    model = ProductGroup

    def get_context_data(self,**kwargs):
        context = super(ProductGroupList, self).get_context_data(**kwargs)
        try:
            company = self.get_company()
        except (Company.DoesNotExist, UserProfile.DoesNotExist):
            company = False
        context['company'] = company
        return context


class AddProductGroup(CreateView, CompanyMixin):
    model = ProductGroup
    form_class = ProductGroupForm
    template_name = 'products/add_edit_product_group.html'
    success_url = '/products/product_groups/'

    def form_valid(self, form):
        new_group = form.save(commit=False)
        new_group.company = self.get_company()
        new_group.save()
        return super(AddProductGroup,self).form_valid(form)

    def get_context_data(self,**kwargs):
        context = super(AddProductGroup, self).get_context_data(**kwargs)
        try:
            company = self.get_company()
        except (Company.DoesNotExist, UserProfile.DoesNotExist):
            company = False
        context['company'] = company
        return context


class UpdateProductGroup(UpdateView):
    model = ProductGroup
    form_class = ProductGroupForm
    template_name = 'products/add_edit_product_group.html'
    pk_url_kwarg = 'group_id'
    success_url = '/products/all/'

    def get_context_data(self,**kwargs):
        context = super(UpdateProductGroup,self).get_context_data(**kwargs)
        context['edit'] = True
        return context


class DeleteProductGroup(DeleteView):
    model = ProductGroup
    form_class = ProductForm
    template_name = 'products/delete_product_group.html'
    pk_url_kwarg = 'group_id'
    success_url = '/products/all/'


# JS-GRID
class ProductListJson(LoginRequiredMixin, CompanyMixin, ListView):
    def GetProductsJson(self):
        try:
            user = self.user
            company = user.userprofile.company
            currency_filter = self.GET.get('currency')
            price_filter = self.GET.get('price')
            code_filter = self.GET.get('code')
            name_filter = self.GET.get('name')
            queryset = Product.objects.filter(company=company)
            if name_filter:
                queryset = queryset.filter(name__contains=name_filter)
            if code_filter:
                queryset = queryset.filter(code__contains=code_filter)
            if currency_filter:
                queryset = queryset.filter(currency__contains=currency_filter)
            if price_filter and price_filter != '0':
                queryset = queryset.filter(price__contains=price_filter)
        except BaseException as exc:
            queryset = []
        results = Paginator(queryset.order_by('name'), 20)
        return HttpResponse(serializers.serialize("json", [q for q in results.page(1).object_list]),
                            content_type='application/json')


class ProductGroupListJson(LoginRequiredMixin, CompanyMixin, ListView):
    def GetProductGroupsJson(self):
        try:
            user = self.user
            company = user.userprofile.company
            category_filter = self.GET.get('category')
            parent_filter = self.GET.get('parent')
            name_filter = self.GET.get('name')
            queryset = ProductGroup.objects.filter(company=company)
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

# CRUD for Currency
class CurrencyList(ListView, CompanyMixin):
    model = Currency
    template_name = 'products/currencies/currency_list.html'
    context_object_name = 'currency_list'

    def get_queryset(self):
        try:
            queryset = Currency.objects.order_by('name')
        except Currency.DoesNotExist:
            queryset = False
        return queryset

    def get_context_data(self,**kwargs):
        context = super(CurrencyList, self).get_context_data(**kwargs)
        try:
            company = self.get_company()
        except (Company.DoesNotExist, UserProfile.DoesNotExist):
            company = False
        context['company'] = company
        return context

class AjaxableResponseMixin(object):
    
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response

class AddCurrencyView(CreateView):
    model = Currency
    fields = ['name']
    template_name = '/products/currencies/currency_list.html'
    success_url = '/products/currencies/'


class DeleteCurrencyView(DeleteView):
    model = Currency
    template_name = 'products/currencies/currency_list.html'
    pk_url_kwarg = 'cur_id'
    success_url = '/products/currencies/'

class EditCurrencyView(UpdateView, AjaxableResponseMixin):
    model = Currency
    fields = ['name']
    template_name = 'products/currencies/currency_list.html'
    pk_url_kwarg = 'cur_id'
    success_url = '/products/currencies/'

    
# CRUD for Category
class CategoryList(ListView, CompanyMixin):
    model = Category
    template_name = 'products/categories/category_list.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        try:
            queryset = Category.objects.order_by('name')
        except Category.DoesNotExist:
            queryset = False
        return queryset

    def get_context_data(self,**kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        try:
            company = self.get_company()
        except (Company.DoesNotExist, UserProfile.DoesNotExist):
            company = False
        context['company'] = company
        return context

class AddCategoryView(CreateView):
    model = Category
    fields = ['name']
    template_name = '/products/categories/currency_list.html'
    success_url = '/products/categories/'

class EditCategoryView(UpdateView):
    model = Category
    fields = ['name']
    template_name = 'products/categories/category_list.html'
    pk_url_kwarg = 'cat_id'
    success_url = '/products/categories/'


class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'products/categories/category_list.html'
    pk_url_kwarg = 'cat_id'
    success_url = '/products/categories/'


# CRUD for Unit
class UnitList(ListView, CompanyMixin):
    model = Unit
    template_name = 'products/units/unit_list.html'
    context_object_name = 'unit_list'

    def get_queryset(self):
        try:
            queryset = Unit.objects.order_by('name')
        except Unit.DoesNotExist:
            queryset = False
        return queryset

    def get_context_data(self,**kwargs):
        context = super(UnitList, self).get_context_data(**kwargs)
        try:
            company = self.get_company()
        except (Company.DoesNotExist, UserProfile.DoesNotExist):
            company = False
        context['company'] = company
        return context

class AddUnitView(CreateView):
    model = Unit
    fields = ['name']
    template_name = '/products/units/unit_list.html'
    success_url = '/products/units/'

class EditUnitView(UpdateView):
    model = Unit
    fields = ['name']
    template_name = 'products/units/unit_list.html'
    pk_url_kwarg = 'unit_id'
    success_url = '/products/units/'

class DeleteUnitView(DeleteView):
    model = Unit
    template_name = 'products/units/unit_list.html'
    pk_url_kwarg = 'unit_id'
    success_url = '/products/units/'

# CRUD for Tax
class TaxList(ListView, CompanyMixin):
    model = Tax
    template_name = 'products/taxes/tax_list.html'
    context_object_name = 'tax_list'

    def get_queryset(self):
        try:
            queryset = Tax.objects.order_by('value')
        except Tax.DoesNotExist:
            queryset = False
        return queryset

    def get_context_data(self,**kwargs):
        context = super(TaxList, self).get_context_data(**kwargs)
        try:
            company = self.get_company()
        except (Company.DoesNotExist, UserProfile.DoesNotExist):
            company = False
        context['company'] = company
        return context


class AddTaxView(CreateView):
    model = Tax
    fields = ['value']
    template_name = '/products/taxes/tax_list.html'
    success_url = '/products/taxes/'


class EditTaxView(UpdateView):
    model = Tax
    fields = ['value']
    template_name = 'products/taxes/tax_list.html'
    pk_url_kwarg = 'tax_id'
    success_url = '/products/taxes/'


class DeleteTaxView(DeleteView):
    model = Tax
    template_name = 'products/taxes/tax_list.html'
    pk_url_kwarg = 'tax_id'
    success_url = '/products/taxes/'

