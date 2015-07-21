from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserForm
# from contacts.models import Contact
from .permissions import LoginRequiredMixin



class UserList(LoginRequiredMixin, ListView):
	context_objects_name = 'user_list'
	template_name = 'users/user_list.html'
	model = User

	# def get_queryset(self):
	# 	reg_users = User.objects.all()
	# 	prof_users = UserProfile.objects.all()
	# 	for reg_user in reg_users:
	# 		try:
	# 			reg_user.userprofile
	# 		except UserProfile.DoesNotExist:
	# 			UserProfile.objects.create(user=reg_user)
	# 	return reg_users

			

class UserDetail(DetailView):
	context_object_name = 'user_details'
	template_name = 'users/user_details.html'
	pk_url_kwarg = 'user_id'
	model = User


	def get_context_data(self,**kwargs):
		context = super(UserDetail,self).get_context_data(**kwargs)
		context['logging'] = self.request.user
		return context



class UpdateUser(UpdateView):
	# model = UserProfile
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


	def form_valid(self,form):
		user = self.request.user
		form.instance.user = self.request.user
		user.first_name = form.instance.name.split()[0]
		user.last_name = form.instance.name.split()[1]
		user.save()
		return super(UpdateUser,self).form_valid(form)


class DeleteUser(DeleteView):
	model = User
	form_class = UserForm
	template_name = 'users/delete_user.html'
	pk_url_kwarg = 'user_id'
	success_url = '/users/all/'
