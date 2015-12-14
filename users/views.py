from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .forms import UserForm
from .permissions import LoginRequiredMixin
from .models import UserProfile
from companies.views import CompanyMixin


class ProfileView(TemplateView, CompanyMixin):
    template_name = 'registration/profile.html'

    def get_context_data(self,**kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        try:
            company = self.get_company()
        except (Company.DoesNotExist, UserProfile.DoesNotExist):
            company = None
        context['company'] = company
        return context


def createUserProfile(sender, instance, **kwargs):
    """Create a UserProfile object each time a User is created ; and link it.
    """
    UserProfile.objects.get_or_create(user=instance)


post_save.connect(createUserProfile, sender=User)


class UserList(LoginRequiredMixin, ListView):
    context_objects_name = 'user_list'
    template_name = 'users/user_list.html'
    model = User


class UserDetail(DetailView):
    context_object_name = 'user_details'
    template_name = 'users/user_details.html'
    pk_url_kwarg = 'user_id'
    model = User

    def get_context_data(self, **kwargs):
        context = super(UserDetail, self).get_context_data(**kwargs)
        context['logging'] = self.request.user
        return context


class UpdateUser(UpdateView):
    form_class = UserForm
    template_name = 'users/edit_user.html'
    pk_url_kwarg = 'user_id'
    success_url = '/users/all/'

    def get_queryset(self):
        user = self.request.user
        try:
            user.userprofile
        except UserProfile.DoesNotExist:
            UserProfile.objects.create(user=user)
        queryset = UserProfile.objects.all()
        return queryset

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = self.request.user
        user.first_name = form.instance.name.split()[0]
        user.last_name = form.instance.name.split()[1]
        user.save()
        return super(UpdateUser, self).form_valid(form)


class DeleteUser(DeleteView):
    model = User
    form_class = UserForm
    template_name = 'users/delete_user.html'
    pk_url_kwarg = 'user_id'
    success_url = '/users/all/'
