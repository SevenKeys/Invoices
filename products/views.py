from django.shortcuts import render
# from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from products.models import Product, ProductGroup
from users.models import UserProfile
# from json import dumps
from .forms import ProductForm, ProductGroupForm
# from common.components.sortable_list import SortableListView
from users.permissions import LoginRequiredMixin
from companies.views import CompanyMixin
# from django.views.generic import TemplateView


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


class ProductDetails(DetailView):
    model = Product
    template_name = 'products/product_details.html'
    pk_url_kwarg = 'product_id'



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
        # user = self.request.user
        # company = user.userprofile.company
        new_group.company = self.get_company()
        new_group.save()
        return super(AddProductGroup,self).form_valid(form)



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

# AJAX search function
def searchProdAjax(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
    else:
        search_text = ''
    products = Product.objects.filter(name__icontains=search_text)
    context = {};
    context['products'] = products

    return render(request, 'products/search_products_results.html', context)
