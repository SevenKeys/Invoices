from django.conf.urls import url
from .views import ProductList, AddProduct, UpdateProduct, DeleteProduct
from .views import AddProductGroup, UpdateProductGroup
from .views import DeleteProductGroup
from .views import ProductListJson, ProductGroupListJson
from .views import CurrencyList, AddCurrencyView, DeleteCurrencyView
from .views import CategoryList
from .views import UnitList

urlpatterns = [
    url(r'^all/$', ProductList.as_view(), 
        name='products'),
    url(r'^add/$', AddProduct.as_view(), 
        name='add_product'),
    url(r'^edit/(?P<product_id>\d+)/$', UpdateProduct.as_view(), 
        name='edit_product'),
    url(r'^delete/(?P<product_id>\d+)/$', DeleteProduct.as_view(), 
        name='delete_product'),
    url(r'^add_group/$', AddProductGroup.as_view(), 
        name='add_product_group'),
    url(r'^edit_group/(?P<group_id>\d+)/$', UpdateProductGroup.as_view(), 
        name='edit_product_group'),
    url(r'^delete_group/(?P<group_id>\d+)/$', DeleteProductGroup.as_view(), 
        name='delete_product_group'),
    url(r'^list/', ProductListJson.GetProductsJson),
    url(r'^list_group/', ProductGroupListJson.GetProductGroupsJson),
    # CRUD for product currencies
    url(r'^currencies/$', CurrencyList.as_view(), 
        name='product_currencies'),
    url(r'^add_currency/$', AddCurrencyView.as_view(), 
        name='add_currency'),
    url(r'^delete_currency/(?P<cur_id>\d+)/$', DeleteCurrencyView.as_view(), 
        name='delete_currency'),
    url(r'^categories/$', CategoryList.as_view(), 
        name='product_categories'),
    url(r'^units/$', UnitList.as_view(), 
        name='product_units')
]
