from django.conf.urls import url
from .views import CustomerList
from .views import AddCustomer, DeleteCustomer, UpdateCustomer
from .views import CustomerGroupList, AddCustomerGroup, CustomerGroupDetail 
from .views import UpdateCustomerGroup, DeleteCustomerGroup
from .views import CustomerListJson, CustomerGroupListJson
from .views import LanguageListView, LanguageAddView, LanguageEditView
from .views import LanguageDeleteView
from .views import ClientTypeListView, ClientTypeAddView, ClientTypeEditView
from .views import ClientTypeDeleteView
from .views import CustCatListView, CustCatAddView, CustCatEditView
from .views import CustCatDeleteView


urlpatterns = [
    # CRUD for customers
    url(r'^all/$', CustomerList.as_view(), 
        name='customers'),
    url(r'^add_customer/$', AddCustomer.as_view(), 
        name='add_customer'),
    url(r'^edit/(?P<customer_id>\d+)/$', UpdateCustomer.as_view(), 
        name='edit_customer'),
    url(r'^delete/(?P<customer_id>\d+)/$', DeleteCustomer.as_view(), 
        name='delete_customer'),
    url(r'^list/', CustomerListJson.GetCustomersJson),
    # CRUD for customer groups
    url(r'^groups/$', CustomerGroupList.as_view(), 
        name='customer_groups'),
    url(r'^add_customer_group/$', AddCustomerGroup.as_view(), 
        name='add_group'),
    url(r'^get_group/(?P<customer_group_id>\d+)/$', CustomerGroupDetail.as_view(), 
        name='get_customer_group'),
    url(r'^edit_group/(?P<customer_group_id>\d+)/$', UpdateCustomerGroup.as_view(), 
        name='edit_customer_group'),
    url(r'^delete_group/(?P<customer_group_id>\d+)/$', DeleteCustomerGroup.as_view(), 
        name='delete_customer_group'),
    url(r'^list_group/', CustomerGroupListJson.GetCustomerGroupsJson),
    # CRUD for language
    url(r'^languages/$', LanguageListView.as_view(), 
        name='languages'),
    url(r'^add_language/$', LanguageAddView.as_view(), 
        name='add_language'),
    url(r'^edit_language/(?P<language_id>\d+)/$', LanguageEditView.as_view(), 
        name='edit_language'),
    url(r'^delete_language/(?P<language_id>\d+)/$', LanguageDeleteView.as_view(), 
        name='delete_language'),
    # CRUD for client types
    url(r'^client_types/$', ClientTypeListView.as_view(), 
        name='client_types'),
    url(r'^add_client_type/$', ClientTypeAddView.as_view(), 
        name='add_client_type'),
    url(r'^edit_client_type/(?P<client_type_id>\d+)/$', ClientTypeEditView.as_view(), 
        name='edit_client_type'),
    url(r'^delete_client_type/(?P<client_type_id>\d+)/$', ClientTypeDeleteView.as_view(), 
        name='delete_client_type'),
    # CRUD for customer group categories
    url(r'^customer_categories/$', CustCatListView.as_view(), 
        name='customer_categories'),
    url(r'^add_customer_category/$', CustCatAddView.as_view(), 
        name='add_customer_category'),
    url(r'^edit_customer_category/(?P<cust_cat_id>\d+)/$', CustCatEditView.as_view(), 
        name='edit_customer_category'),
    url(r'^delete_customer_category/(?P<cust_cat_id>\d+)/$', CustCatDeleteView.as_view(), 
        name='delete_customer_category')
]
