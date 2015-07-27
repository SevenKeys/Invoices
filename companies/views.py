# from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.http import HttpResponse
from .models import Company
from .forms import CompanyForm
from contacts.models import Contact
from users.models import UserProfile
from users.permissions import LoginRequiredMixin

# Mixin to get company of user
class CompanyMixin(object):

    def get_company(self,**kwargs):
        user = self.request.user
        company = user.userprofile.company
        return company


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
	success_url = '/'

	def form_invalid(self,form):
		return HttpResponse('form is invalid')

	def form_valid(self,form):
		new_company = form.save(commit=False)
		# create Contact model
		contact = Contact(phone_number=self.request.POST['phone_number'],
						  email=self.request.POST['email'],
						  street=self.request.POST['street'],
						  city=self.request.POST['city'],
						  postcode=self.request.POST['postcode'],
						  country=self.request.POST['country'],
						  website=self.request.POST['website'])
		contact.save()
		new_company.contact = contact
		# define user has userprofile or create it
		try:
			self.request.user.userprofile
		except UserProfile.DoesNotExist:
			UserProfile.objects.create(user=self.request.user,
									   name=self.request.POST['user_name'])
		
		new_company.save()
		# connect the new company with user
		name = self.request.user.userprofile.name
		user = UserProfile.objects.get(name=name)
		new_company.userprofile_set.add(user)
		return super(AddCompany, self).form_valid(form)


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
