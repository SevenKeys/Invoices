from django.conf.urls import url, include
from .views import CompanyDetail, AddCompany, UpdateCompany, DeleteCompany

urlpatterns = [
	url(r'^company_details/(?P<company_id>\d+)/$', CompanyDetail.as_view(),name='company_details'),
	url(r'^add_company/$', AddCompany.as_view(),name='add_company'),
	url(r'^edit_company/(?P<company_id>\d+)/$', UpdateCompany.as_view(),name='edit_company'),
	url(r'^delete_company/(?P<company_id>\d+)/$', DeleteCompany.as_view(),name='delete_company')
]