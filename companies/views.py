# from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.http import HttpResponse
from .models import Company
from .forms import CompanyForm
# from contacts.models import Contact
from users.models import UserProfile
from users.permissions import LoginRequiredMixin



class CompanyList(LoginRequiredMixin, ListView):
	context_objects_name = 'company_list'
	template_name = 'companies/company_list.html'
	model = Company
	# To check user has userprofile to create company
	def get_context_data(self,**kwargs):
		context = super(CompanyList,self).get_context_data(**kwargs)
		user = self.request.user
		context['user'] = user
		return context
	


class CompanyDetail(DetailView):
	context_object_name = 'company_details'
	template_name = 'companies/company_detail.html'
	pk_url_kwarg = 'company_id'
	model = Company
	# To check access to update and delete company
	def get_context_data(self,**kwargs):
		context = super(CompanyDetail, self).get_context_data(**kwargs)
		user = self.request.user
		company = self.get_object()
		try:
			user_company = user.userprofile.company
		except UserProfile.DoesNotExist:
			company = None
		if company == user_company:
			context['match'] = True
		return context

	
class AddCompany(CreateView):
	model = Company
	form_class = CompanyForm
	template_name = 'companies/edit_company.html'
	success_url = '/companies/all/'

	def form_invalid(self,form):
		return HttpResponse('form is invalid')


class UpdateCompany(UpdateView):
	model = Company
	form_class = CompanyForm
	template_name = 'companies/edit_company.html'
	pk_url_kwarg = 'company_id'
	success_url = '/companies/all/'


class DeleteCompany(DeleteView):
	model = Company
	form_class = CompanyForm
	template_name = 'companies/delete_company.html'
	pk_url_kwarg = 'company_id'
	success_url = '/companies/all/'
