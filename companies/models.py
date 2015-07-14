from django.db import models
from contacts.models import Contact


class Company(models.Model):
    name = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    contact = models.ForeignKey(Contact, blank=True, null=True)
    reg_code = models.CharField(max_length=30)

    def __str__(self):
    	return self.name
# Create your models here.
