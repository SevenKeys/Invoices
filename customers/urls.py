from django.conf.urls import url
from .views import CustomerList
from .views import AddCustomer, DeleteCustomer, UpdateCustomer
from .views import AddCustomerGroup, CustomerGroupDetail, DeleteCustomerGroup, UpdateCustomerGroup
from .views import SearchCustAjax

urlpatterns = [
    url(r'^all/$', CustomerList.as_view(), name='customers'),
    url(r'^add_customer/$', AddCustomer.as_view(), name='add_customer'),
    url(r'^edit/(?P<customer_id>\d+)/$', UpdateCustomer.as_view(), name='edit_customer'),
    url(r'^delete/(?P<customer_id>\d+)/$', DeleteCustomer.as_view(), name='delete_customer'),
    url(r'^add_group/$', AddCustomerGroup.as_view(), name='add_group'),
    url(r'^get_group/(?P<group_id>\d+)/$', CustomerGroupDetail.as_view(), name='get_group'),
    url(r'^edit_group/(?P<group_id>\d+)/$', UpdateCustomerGroup.as_view(), name='edit_group'),
    url(r'^delete_group/(?P<group_id>\d+)/$', DeleteCustomerGroup.as_view(), name='delete_group'),
    url(r'^search/$', SearchCustAjax)
]
