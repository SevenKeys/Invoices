from django import forms
from .models import UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):

	class Meta:
		model = UserProfile
		fields = ['company','contact']
