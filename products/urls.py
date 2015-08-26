from django.conf.urls import url
from .views import ProductList, AddProduct, SuccessProduct
from .views import UpdateProduct, DeleteProduct
from .views import ProductGroupList, AddProductGroup, SuccessProductGroup
from .views import DeleteProductGroup, UpdateProductGroup
from .views import ProductListJson, ProductGroupListJson
from .views import CurrencyList, EditCurrencyView, AddCurrencyView, DeleteCurrencyView
from .views import CategoryList, EditCategoryView, AddCategoryView, DeleteCategoryView
from .views import UnitList, AddUnitView, EditUnitView, DeleteUnitView
from .views import TaxList, AddTaxView, EditTaxView, DeleteTaxView
from .views import GroupCatList, AddGroupCategoryView
from .views import EditGroupCategoryView, DeleteGroupCategoryView

urlpatterns = [
    url(r'^all/$', ProductList.as_view(), 
        name='products'),
    url(r'^add/$', AddProduct.as_view(), 
        name='add_product'),
    url(r'^success/$', SuccessProduct.as_view(), 
        name='success_product'),
    url(r'^edit/(?P<product_id>\d+)/$', UpdateProduct.as_view(), 
        name='edit_product'),
    url(r'^delete/(?P<product_id>\d+)/$', DeleteProduct.as_view(), 
        name='delete_product'),
    # CRUD for Product group app
    url(r'^groups/$', ProductGroupList.as_view(),
        name='product_groups'),
    url(r'^add_group/$', AddProductGroup.as_view(), 
        name='add_product_group'),
    url(r'^success_group/$', SuccessProductGroup.as_view(), 
        name='success_product_group'),
    url(r'^edit_group/(?P<group_id>\d+)/$', UpdateProductGroup.as_view(), 
        name='edit_product_group'),
    url(r'^delete_group/(?P<group_id>\d+)/$', DeleteProductGroup.as_view(), 
        name='delete_product_group'),
    url(r'^list/', ProductListJson.GetProductsJson),
    url(r'^list_group/', ProductGroupListJson.GetProductGroupsJson),
    # CRUD for ProductGroup categories
    url(r'^group_categories/$', GroupCatList.as_view(), 
        name='product_group_categories'),
    url(r'^add_group_category/$', AddGroupCategoryView.as_view(), 
        name='add_group_category'),
    url(r'^delete_group_category/(?P<group_cat_id>\d+)/$', DeleteGroupCategoryView.as_view(), 
        name='delete_group_category'),
    url(r'^edit_group_category/(?P<group_cat_id>\d+)/$', EditGroupCategoryView.as_view(), 
        name='edit_group_category'),
    # CRUD for product currencies
    url(r'^currencies/$', CurrencyList.as_view(), 
        name='product_currencies'),
    url(r'^add_currency/$', AddCurrencyView.as_view(), 
        name='add_currency'),
    url(r'^delete_currency/(?P<cur_id>\d+)/$', DeleteCurrencyView.as_view(), 
        name='delete_currency'),
    url(r'^edit_currency/(?P<cur_id>\d+)/$', EditCurrencyView.as_view(), 
        name='edit_currency'),
    # CRUD for product categories
    url(r'^categories/$', CategoryList.as_view(), 
        name='product_categories'),
    url(r'^add_category/$', AddCategoryView.as_view(), 
        name='add_category'),
    url(r'^delete_category/(?P<cat_id>\d+)/$', DeleteCategoryView.as_view(), 
        name='delete_category'),
    url(r'^edit_category/(?P<cat_id>\d+)/$', EditCategoryView.as_view(), 
        name='edit_category'),
    # CRUD for product units of measure
    url(r'^units/$', UnitList.as_view(), 
        name='product_units'),
    url(r'^add_unit/$', AddUnitView.as_view(), 
        name='add_unit'),
    url(r'^delete_unit/(?P<unit_id>\d+)/$', DeleteUnitView.as_view(), 
        name='delete_unit'),
    url(r'^edit_unit/(?P<unit_id>\d+)/$', EditUnitView.as_view(), 
        name='edit_unit'),
    # CRUD for product taxes
    url(r'^taxes/$', TaxList.as_view(), 
        name='product_taxes'),
    url(r'^add_tax/$', AddTaxView.as_view(), 
        name='add_tax'),
    url(r'^delete_tax/(?P<tax_id>\d+)/$', DeleteTaxView.as_view(), 
        name='delete_tax'),
    url(r'^edit_tax/(?P<tax_id>\d+)/$', EditTaxView.as_view(), 
        name='edit_tax')
]
