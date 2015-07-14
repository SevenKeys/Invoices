from django.db import models
from companies.models import Company
from contacts.models import Contact


class Customer(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now=True)
    contact = models.ForeignKey(Contact, null=True)

    def __str__(self):
        return self.name


class CustomerDetails(models.Model):
    customer = models.ForeignKey(Customer)
    field_name = models.CharField(max_length=100)
    field_value = models.CharField(max_length=100)

    def __str__(self):
        return self.field_name


class CustomerGroup(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=100)
    customers = models.ManyToManyField(Customer)

    def __str__(self):
        return self.name