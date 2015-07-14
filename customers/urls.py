from django.conf.urls import include, url
from .views import CustomerList, CustomerDetail, CustomerGroup
from .views import AddCustomer, DeleteCustomer, UpdateCustomer

urlpatterns = [
	url(r'^all/$',CustomerList.as_view(),name='customers'),
	url(r'^get/(?P<customer_id>\w+)/$',CustomerDetail.as_view(),name='customer-detail'),
	url(r'^add/$', AddCustomer.as_view(),name='add-customer'),
	url(r'^edit/(?P<customer_id>\d+)/$', UpdateCustomer.as_view(),name='edit-customer'),
	url(r'^delete/(?P<customer_id>\d+)/$', DeleteCustomer.as_view(),name='delete-customer')
]