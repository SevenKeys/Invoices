from django.conf.urls import url
from .views import ProductList, AddProduct, UpdateProduct, DeleteProduct
from .views import ProductGroupDetail, AddProductGroup, UpdateProductGroup, DeleteProductGroup
from .views import searchProdAjax

urlpatterns = [
    url(r'^all/$', ProductList.as_view(), name='products'),
    url(r'^add/$', AddProduct.as_view(), name='add_product'),
    url(r'^edit/(?P<product_id>\d+)/$', UpdateProduct.as_view(), name='edit_product'),
    url(r'^delete/(?P<product_id>\d+)/$', DeleteProduct.as_view(), name='delete_product'),
    url(r'^product_group/(?P<group_id>\d+)/$', ProductGroupDetail.as_view(), name='product_group'),
    url(r'^add_group/$', AddProductGroup.as_view(), name='add_product_group'),
    url(r'^edit_group/(?P<group_id>\d+)/$', UpdateProductGroup.as_view(), name='edit_product_group'),
    url(r'^delete_group/(?P<group_id>\d+)/$', DeleteProductGroup.as_view(), name='delete_product_group'),
    url(r'^search/$', searchProdAjax)

]
