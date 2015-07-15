from django.conf.urls import url, include
from .views import ProductList, ProductListView, ClientListView
from .views import AddProduct, UpdateProduct, DeleteProduct

urlpatterns = [
    url(r'^all/$', ProductList.as_view(), name='products'),
    url(r'^groups/$', ProductListView.as_view(), name='product_list'),
    url(r'^client_groups/', ClientListView.as_view(), name='client_list'),
    url(r'^add/$', AddProduct.as_view(), name='add_product'),
    url(r'^edit/(?P<product_id>\d+)/$', UpdateProduct.as_view(), name='edit_product'),
    url(r'^delete/(?P<product_id>\d+)/$', DeleteProduct.as_view(), name='delete_product')
]