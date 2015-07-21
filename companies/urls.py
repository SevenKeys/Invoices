from django.conf.urls import url, include
from .views import CompanyList, CompanyDetail, AddCompany, UpdateCompany, DeleteCompany

urlpatterns = [
	url(r'^all/$', CompanyList.as_view(),name='companies'),
	url(r'^company_detail/(?P<company_id>\d+)/$', CompanyDetail.as_view(),name='company_detail'),
	url(r'^add_company/$', AddCompany.as_view(),name='add_company'),
	url(r'^edit_company/(?P<company_id>\d+)/$', UpdateCompany.as_view(),name='edit_company'),
	url(r'^delete_company/(?P<company_id>\d+)/$', DeleteCompany.as_view(),name='delete_company')
]