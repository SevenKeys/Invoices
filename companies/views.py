# from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from .models import Company, CompanySegment
from .forms import CompanyForm, SegmentForm
from contacts.models import Contact
from contacts.views import ContactMixin
from users.models import UserProfile
from users.permissions import LoginRequiredMixin


# Mixin to get company of user
class CompanyMixin(object):
    model = Company

    def get_company(self):
        user = self.request.user
        company = user.userprofile.company
        return company
        
    def get_context_data(self,**kwargs):
        context = super(CompanyMixin,self).get_context_data(**kwargs)
        try:
            user = self.request.user
            company = user.userprofile.company
        except (UserProfile.DoesNotExist, Company.DoesNotExist, AttributeError):
            company = False
        context['company'] = company
        return context


# add company id to navigation menu
class NavMenuView(CompanyMixin, TemplateView):
    template_name = 'index.html'


class CompanyDetail(DetailView, LoginRequiredMixin, CompanyMixin):
    template_name = 'companies/company_detail.html'
    pk_url_kwarg = 'company_id'
    model = Company

    
class AddCompany(CreateView, ContactMixin):
    model = Company
    form_class = CompanyForm
    template_name = 'companies/add_edit_company.html'
    success_url = '/'

    def form_valid(self,form):
        new_company = form.save(commit=False)
        
        # get from request Contact data
        contact = Contact(phone_number=self.request.POST['phone_number'],
                          email=self.request.POST['email'],
                          street=self.request.POST['street'],
                          city=self.request.POST['city'],
                          postcode=self.request.POST['postcode'],
                          country=self.request.POST['country'],
                          website=self.request.POST['website'])
        contact.save()
        # write user's first and last names
        full_name = self.request.POST['full_user_name']
        register_user = self.request.user
        if len(full_name.split(' '))==2:
            print('name is twofold')
            register_user.first_name = full_name.split(' ')[0] 
            register_user.last_name = full_name.split(' ')[1]
            register_user.save()

        # connect the new company with Contact model
        new_company.contact = contact
        new_company.save()
        # connect data - company, user and contact
        current_user = UserProfile.objects.get(user=register_user)
        current_user.name = full_name
        new_company.userprofile_set.add(current_user)

        contact.userprofile_set.add(current_user)
        return super(AddCompany, self).form_valid(form)

    
    def get_form_kwargs(self, **kwargs):
        kwargs = super(AddCompany, self).get_form_kwargs(**kwargs)
        kwargs.update({
            'user': self.request.user
            })
        return kwargs



class UpdateCompany(UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'companies/add_edit_company.html'
    pk_url_kwarg = 'company_id'
    # success_url = '/'

    def get_form_kwargs(self, **kwargs):
        kwargs = super(UpdateCompany, self).get_form_kwargs(**kwargs)
        kwargs.update({
            'user': self.request.user
            })
        return kwargs
    # change header in form
    def get_context_data(self, **kwargs):
        context = super(UpdateCompany, self).get_context_data(**kwargs)
        context['edit'] = True
        return context

    def get_success_url(self):
        return reverse('get_company',kwargs={'company_id':self.object.pk})


class DeleteCompany(DeleteView):
    model = Company
    form_class = CompanyForm
    template_name = 'companies/delete_company.html'
    pk_url_kwarg = 'company_id'
    success_url = '/companies/success_delete/'
    
    
class SuccessDelete(TemplateView):
    template_name = 'companies/success_delete.html'

