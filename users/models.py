from django.db import models
from django.contrib.auth.models import User
from companies.models import Company
from contacts.models import Contact

# Create your models here.
class UserProfile(models.Model):
    company = models.ForeignKey(Company, blank=True, null=True)
    name = models.CharField(max_length=60)
    user = models.OneToOneField(User)
    created = models.DateTimeField(auto_now=True)
    contact = models.ForeignKey(Contact, null=True)
