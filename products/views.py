from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from products.models import Product
from users.models import User
from json import dumps
from .forms import ProductForm
from common.components.sortable_list import SortableListView
from users.permissions import LoginRequiredMixin
from django.views.generic import TemplateView


class ProductListView(SortableListView):
    def __init__(self):
        super(ProductListView, self).__init__()

    def get_groups(self):
        # add DB reading
        return super(ProductListView, self).get_test_groups()


class ClientListView(SortableListView):  # todo: move this to clients view
    def __init__(self):
        super(ClientListView, self).__init__()
        self.get_groups()

    def get_groups(self):
        return super(ClientListView, self).get_test_groups()  # todo: load groups from DB


# Create your views here.

class ProductView(TemplateView):
    template_name = 'main_logged_in/products.html'

    def create_new(request):
        if request.method == 'POST':
            response_data = {}

            product = Product(company='test', name='test')
            product.save()

            response_data['result'] = 'OK'
            response_data['company'] = product.company
            response_data['name'] = product.name

            return HttpResponse(
                dumps(response_data),
                content_type="application/json"
            )

# CRUD for Product app
class ProductList(LoginRequiredMixin, ListView):
    context_oject_name = 'product_list'
    template_name = 'products/product_list.html'

    def get_queryset(self):
        try:
            user = User.objects.get(username=self.request.user)
            if user:
                company = user.userprofile.company
                return Product.objects.filter(company=company)
            else:
                return False
        except User.DoesNotExist:
            return False


class AddProduct(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/edit_product.html'
    success_url = '/products/all/'


    def form_invalid(self,form):
        return HttpResponse('form is invalid')


class UpdateProduct(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/edit_product.html'
    pk_url_kwarg = 'product_id'
    success_url = '/products/all/'


class DeleteProduct(DeleteView):
    model = Product
    form_class = ProductForm
    template_name = 'products/delete_product.html'
    pk_url_kwarg = 'product_id'
    success_url = '/products/all/'