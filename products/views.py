from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.core import serializers
from companies.models import Company
from .models import Product, ProductGroup, ProductGroupCategory
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


class AddProduct(CompanyMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/add_edit_product.html'
    success_url = '/products/success/'

    def form_valid(self, form):
        new_product = form.save(commit=False)
        new_product.company = self.get_company()
        cur = self.request.POST['currency']
        if cur == '':
            new_cur = Currency.objects.get_or_create(name='None')
            new_product.currency = new_cur[0]
        unit = self.request.POST['unit']
        if unit == '':
            new_unit = Unit.objects.get_or_create(name='None')
            new_product.unit = new_unit[0]
        new_product.save()
        return super(AddProduct,self).form_valid(form)

    def get_context_data(self,**kwargs):
        context = super(AddProduct, self).get_context_data(**kwargs)
        context['add'] = True
        return context


class SuccessProduct(TemplateView):
    template_name = 'products/add_product_success.html'


class UpdateProduct(CompanyMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/add_edit_product.html'
    pk_url_kwarg = 'product_id'
    success_url = '/products/success/'

    def form_valid(self, form):
        new_product = form.save(commit=False)
        cur = self.request.POST['currency']
        if cur == '':
            new_cur = Currency.objects.get_or_create(name='None')
            new_product.currency = new_cur[0]
        unit = self.request.POST['unit']
        if unit == '':
            new_unit = Unit.objects.get_or_create(name='None')
            new_product.unit = new_unit[0]
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
    template_name = 'products/product_groups/product_group_list.html'
    model = ProductGroup


class AddProductGroup(CompanyMixin, CreateView):
    model = ProductGroup
    form_class = ProductGroupForm
    template_name = 'products/product_groups/add_edit_product_group.html'
    success_url = '/products/success_group/'

    def form_valid(self, form):
        new_group = form.save(commit=False)
        new_group.company = self.get_company()
        cat = self.request.POST['category']
        if cat == '':
            new_cat = ProductGroupCategory.objects.get_or_create(name='None')
            new_group.category = new_cat[0]
        new_group.save()
        return super(AddProductGroup,self).form_valid(form)


class SuccessProductGroup(TemplateView):
    template_name = 'products/product_groups/add_group_success.html'


class UpdateProductGroup(UpdateView):
    model = ProductGroup
    form_class = ProductGroupForm
    template_name = 'products/product_groups/add_edit_product_group.html'
    pk_url_kwarg = 'group_id'
    success_url = '/products/success_group/'

    def get_context_data(self,**kwargs):
        context = super(UpdateProductGroup,self).get_context_data(**kwargs)
        context['edit'] = True
        return context

    def form_valid(self, form):
        new_group = form.save(commit=False)
        cat = self.request.POST['category']
        if cat == '':
            new_cat = ProductGroupCategory.objects.get_or_create(name='None')
            new_group.category = new_cat[0]
        new_group.save()
        return super(UpdateProductGroup,self).form_valid(form)


class DeleteProductGroup(DeleteView):
    model = ProductGroup
    form_class = ProductForm
    template_name = 'products/product_groups/delete_product_group.html'
    pk_url_kwarg = 'group_id'
    success_url = '/products/groups/'


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
        return HttpResponse(serializers.serialize("json", [q for q in results.page(1).object_list],
                                                  use_natural_foreign_keys=True),
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
        return HttpResponse(serializers.serialize("json", [q for q in results.page(1).object_list],
                                                  use_natural_foreign_keys=True),
                            content_type='application/json')


class ProductListsJson(LoginRequiredMixin, CompanyMixin, ListView):
    def GetCurrencyJson(self):
        try:
            name_filter = self.GET.get('name')
            queryset = Currency.objects.exclude(name='None')
            if name_filter:
                queryset = queryset.filter(name__contains=name_filter)
        except BaseException as exc:
            queryset = []
        results = Paginator(queryset.order_by('name'), 20)
        return HttpResponse(serializers.serialize("json", [q for q in results.page(1).object_list]),
                            content_type='application/json')
                       
    def GetCategoryJson(self):
        try:
            name_filter = self.GET.get('name')
            queryset = Category.objects.all()
            if name_filter:
                queryset = queryset.filter(name__contains=name_filter)
        except BaseException as exc:
            queryset = []
        results = Paginator(queryset.order_by('name'), 20)
        return HttpResponse(serializers.serialize("json", [q for q in results.page(1).object_list]),
                            content_type='application/json')
                            
    def GetUnitJson(self):
        try:
            name_filter = self.GET.get('name')
            queryset = Unit.objects.exclude(name='None')
            if name_filter:
                queryset = queryset.filter(name__contains=name_filter)
        except BaseException as exc:
            queryset = []
        results = Paginator(queryset.order_by('name'), 20)
        return HttpResponse(serializers.serialize("json", [q for q in results.page(1).object_list]),
                            content_type='application/json')
                            
    def GetTaxJson(self):
        try:
            value_filter = self.GET.get('value')
            value_filter = int(value_filter)
            queryset = Tax.objects.all()
            if value_filter:
                queryset = queryset.filter(value=value_filter)
        except BaseException as exc:
            queryset = []
        results = Paginator(queryset.order_by('value'), 20)
        print(queryset)
        return HttpResponse(serializers.serialize("json", [q for q in results.page(1).object_list]),
                            content_type='application/json')
                            
                            
class ProductGroupListsJson(LoginRequiredMixin, CompanyMixin, ListView):
    def GetCategoryJson(self):
        try:
            name_filter = self.GET.get('name')
            queryset = ProductGroupCategory.objects.all()
            if name_filter:
                queryset = queryset.filter(name__contains=name_filter)
        except BaseException as exc:
            queryset = []
        results = Paginator(queryset.order_by('name'), 20)
        return HttpResponse(serializers.serialize("json", [q for q in results.page(1).object_list]),
                            content_type='application/json')


# CRUD for Currency
class CurrencyList(CompanyMixin, ListView):
    model = Currency
    template_name = 'products/currencies/currency_list.html'



class AddCurrencyView(CreateView):
    model = Currency
    fields = ['name']
    template_name = 'products/currencies/add_edit_currency.html'
    success_url = '/products/success_currency/'


class SuccessCurrency(TemplateView):
    template_name = 'products/currencies/currency_success.html'
    
    
class DeleteCurrencyView(DeleteView):
    model = Currency
    template_name = 'products/currencies/currency_list.html'
    pk_url_kwarg = 'cur_id'
    success_url = '/products/success_currency/'


class EditCurrencyView(UpdateView):
    model = Currency
    fields = ['name']
    template_name = 'products/currencies/add_edit_currency.html'
    pk_url_kwarg = 'cur_id'
    success_url = '/products/currency_success/'
    
    def get_context_data(self, **kwargs):
        context = super(EditCurrencyView, self).get_context_data(**kwargs)
        context['edit'] = True
        return context

    
# CRUD for Category
class CategoryList(CompanyMixin, ListView):
    model = Category
    template_name = 'products/categories/category_list.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        try:
            queryset = Category.objects.order_by('name')
        except Category.DoesNotExist:
            queryset = False
        return queryset


class AddCategoryView(CreateView):
    model = Category
    fields = ['name']
    template_name = 'products/categories/add_edit_category.html'
    success_url = '/products/success_category/'


class SuccessCategory(TemplateView):
    template_name = 'products/categories/success_category.html'
    
    
class EditCategoryView(UpdateView):
    model = Category
    fields = ['name']
    template_name = 'products/categories/add_edit_category.html'
    pk_url_kwarg = 'cat_id'
    success_url = '/products/success_category/'
    
    def get_context_data(self, **kwargs):
        context = super(EditCategoryView, self).get_context_data(**kwargs)
        context['edit'] = True
        return context


class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'products/categories/category_list.html'
    pk_url_kwarg = 'cat_id'
    success_url = '/products/categories/'


# CRUD for Unit
class UnitList(CompanyMixin, ListView):
    model = Unit
    template_name = 'products/units/unit_list.html'
    context_object_name = 'unit_list'

    def get_queryset(self):
        try:
            queryset = Unit.objects.order_by('name')
        except Unit.DoesNotExist:
            queryset = False
        return queryset


class AddUnitView(CreateView):
    model = Unit
    fields = ['name']
    template_name = 'products/units/add_edit_unit.html'
    success_url = '/products/success_unit/'


class SuccessUnit(TemplateView):
    template_name = 'products/units/success_unit.html'
    


class EditUnitView(UpdateView):
    model = Unit
    fields = ['name']
    template_name = 'products/units/add_edit_unit.html'
    pk_url_kwarg = 'unit_id'
    success_url = '/products/success_unit/'
    
    def get_context_data(self, **kwargs):
        context = super(EditUnitView, self).get_context_data(**kwargs)
        context['edit'] = True
        return context



class DeleteUnitView(DeleteView):
    model = Unit
    template_name = 'products/units/unit_list.html'
    pk_url_kwarg = 'unit_id'
    success_url = '/products/units/'


# CRUD for Tax
class TaxList(CompanyMixin, ListView):
    model = Tax
    template_name = 'products/taxes/tax_list.html'


class AddTaxView(CreateView):
    model = Tax
    fields = ['value']
    template_name = 'products/taxes/add_edit_tax.html'
    success_url = '/products/success_tax/'


class SuccessTax(TemplateView):
    template_name = 'products/taxes/success_tax.html'
    
    
class EditTaxView(UpdateView):
    model = Tax
    fields = ['value']
    template_name = 'products/taxes/add_edit_tax.html'
    pk_url_kwarg = 'tax_id'
    success_url = '/products/success_tax/'
    
    def get_context_data(self, **kwargs):
        context = super(EditTaxView, self).get_context_data(**kwargs)
        context['edit'] = True
        return context


class DeleteTaxView(DeleteView):
    model = Tax
    template_name = 'products/taxes/tax_list.html'
    pk_url_kwarg = 'tax_id'
    success_url = '/products/taxes/'


# CRUD for ProductGroupCategory
class GroupCatList(CompanyMixin, ListView):
    model = ProductGroupCategory
    template_name = 'products/product_groups/group_cat_list.html'


class AddGroupCategoryView(CreateView):
    model = ProductGroupCategory
    fields = ['name']
    template_name = 'products/product_groups/add_edit_group_cat.html'
    success_url = '/products/success_group_cat/'
    

class SuccessGroupCat(TemplateView):
    template_name = 'products/product_groups/success_group_cat.html'


class EditGroupCategoryView(UpdateView):
    model = ProductGroupCategory
    fields = ['name']
    template_name = 'products/product_groups/add_edit_group_cat.html'
    pk_url_kwarg = 'group_cat_id'
    success_url = '/products/success_group_cat/'
    
    def get_context_data(self, **kwargs):
        context = super(EditGroupCategoryView, self).get_context_data(**kwargs)
        context['edit'] = True
        return context


class DeleteGroupCategoryView(DeleteView):
    model = ProductGroupCategory
    template_name = 'products/product_groups/prod_group_cat.html'
    pk_url_kwarg = 'group_cat_id'
    success_url = '/products/group_categories/'

