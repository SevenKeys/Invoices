from django.core import serializers
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from products.models import Product, ProductGroup
from users.models import UserProfile
from .forms import ProductForm, ProductGroupForm
from users.permissions import LoginRequiredMixin
from companies.views import CompanyMixin


# CRUD for Product app
class ProductList(LoginRequiredMixin, CompanyMixin, ListView):
    context_oject_name = 'product_list'
    template_name = 'products/product_list.html'

    def get_queryset(self):
        try:
            company = self.get_company()
            queryset = Product.objects.filter(company=company).order_by('name')
        except:
            queryset = False
        return queryset

    def get_context_data(self):
        context = super(ProductList, self).get_context_data()
        try:
            company = self.get_company()
        except UserProfile.DoesNotExist:
            company = False
        context['company'] = company
        return context


class AddProduct(CreateView, CompanyMixin):
    model = Product
    form_class = ProductForm
    template_name = 'products/add_edit_product.html'
    success_url = '/products/all/'

    def form_valid(self, form):
        new_product = form.save(commit=False)
        new_product.company = self.get_company()
        new_product.save()
        return super(AddProduct, self).form_valid(form)


class UpdateProduct(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/add_edit_product.html'
    pk_url_kwarg = 'product_id'
    success_url = '/products/all/'


class DeleteProduct(DeleteView):
    model = Product
    form_class = ProductForm
    template_name = 'products/delete_product.html'
    pk_url_kwarg = 'product_id'
    success_url = '/products/all/'


# CRUD for ProductGroup
class ProductGroupDetail(DetailView):
    model = ProductGroup
    template_name = 'products/product_group.html'
    pk_url_kwarg = 'group_id'


class AddProductGroup(CreateView, CompanyMixin):
    model = ProductGroup
    form_class = ProductGroupForm
    template_name = 'products/add_edit_product_group.html'
    success_url = '/products/all/'

    def form_valid(self, form):
        new_group = form.save(commit=False)
        new_group.company = self.get_company()
        new_group.save()
        return super(AddProductGroup, self).form_valid(form)


class UpdateProductGroup(UpdateView):
    model = ProductGroup
    form_class = ProductGroupForm
    template_name = 'products/add_edit_product_group.html'
    pk_url_kwarg = 'group_id'
    success_url = '/products/all/'

    def get_context_data(self, **kwargs):
        context = super(UpdateProductGroup, self).get_context_data(**kwargs)
        context['edit'] = True
        return context


class DeleteProductGroup(DeleteView):
    model = ProductGroup
    form_class = ProductForm
    template_name = 'products/delete_product_group.html'
    pk_url_kwarg = 'group_id'
    success_url = '/products/all/'


# AJAX search function
def searchProdAjax(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''
    products = Product.objects.filter(name__icontains=search_text)
    context = {'products': products}

    return render(request, 'products/search_products_results.html', context)


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
