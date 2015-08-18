from django.conf.urls import url, include
from .views import CompanyDetail, AddCompany, UpdateCompany, DeleteCompany

urlpatterns = [
	url(r'^get_company/(?P<company_id>\d+)/$', CompanyDetail.as_view(),name='get_company'),
	url(r'^add_company/$', AddCompany.as_view(),name='add_company'),
	url(r'^edit_company/(?P<company_id>\d+)/$', UpdateCompany.as_view(),name='edit_company'),
	url(r'^delete_company/(?P<company_id>\d+)/$', DeleteCompany.as_view(),name='delete_company')
]