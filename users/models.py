from django.db import models
from companies.models import Company
from contacts.models import Contact


class User(models.Model):
    company = models.ForeignKey(Company, blank=True, null=True)
    name = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now=True)
    contact = models.ForeignKey(Contact, null=True)
# Create your models here.
