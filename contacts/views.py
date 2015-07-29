from django.shortcuts import render

# Create your views here.
# mixin to get contact and data
class ContactMixin(object):

	def get_contact(self, **kwargs):
		user = self.request.user
		contact = user.userprofile.contact
		return contact

	# def get_form_kwargs(self, **kwargs):
	# 	kwargs = super(AddCompany, self).get_form_kwargs(**kwargs)
	# 	kwargs.update({
	# 		'user': self.request.user
	# 		})
	# 	return kwargs