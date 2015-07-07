from django.shortcuts import render
from django.template import loader, Context
from django.forms import ModelForm
from django.http import HttpResponse
from products.models import Product
from json import dumps

from common.components.sortable_list import SortableListView

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
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['company', 'name']

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

