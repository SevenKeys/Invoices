from django.conf.urls import include, url
from .views import CustomerList, CustomerDetail, CustomerGroups

urlpatterns = [
	url(r'^all/$',CustomerList.as_view(),name='customers')
	url(r'^get/(?P<customer_id>\d+)/$',CustomerDetail.as_view(),name='customer_detail')
	url(r'^groups/$',CustomerGroups.as_view(),name='customer_groups')
]