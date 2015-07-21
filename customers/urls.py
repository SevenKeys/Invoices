from django.conf.urls import include, url
from .views import CustomerList, CustomerDetail, CustomerGroup
from .views import AddCustomer, DeleteCustomer, UpdateCustomer
from .views import AddCustomerGroup, DeleteCustomerGroup, UpdateCustomerGroup
from .views import AddCustomerDetail, DeleteCustomerDetail, UpdateCustomerDetail

urlpatterns = [
	url(r'^all/$',CustomerList.as_view(),name='customers'),
	url(r'^get/(?P<customer_id>\w+)/$',CustomerDetail.as_view(),name='customer_detail'),
	url(r'^add_customer/$', AddCustomer.as_view(),name='add_customer'),
	url(r'^edit/(?P<customer_id>\d+)/$', UpdateCustomer.as_view(),name='edit-customer'),
	url(r'^delete/(?P<customer_id>\d+)/$', DeleteCustomer.as_view(),name='delete-customer'),
	url(r'^add_detail/(?P<customer_id>\d+)/$', AddCustomerDetail.as_view(),name='add_detail'),
	url(r'^edit_detail/(?P<detail_id>\d+)/$', UpdateCustomerDetail.as_view(),name='edit_detail'),
	url(r'^delete_detail/(?P<detail_id>\d+)/$', DeleteCustomerDetail.as_view(),name='delete_detail'),
	url(r'^add_group/$', AddCustomerGroup.as_view(),name='add_group')
]