from django.db import models
from companies.models import Company
from contacts.models import Contact
from django.contrib.auth.models import User


class UserProfile(models.Model):
    company = models.ForeignKey(Company, blank=True, null=True)
    contact = models.ForeignKey(Contact, null=True)
    user = models.OneToOneField(User)
    name = models.CharField(max_length=120, blank=True, null=True)


    def __str__(self):
    	return self.name
