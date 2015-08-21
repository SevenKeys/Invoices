from django.db import models
from companies.models import Company, CompanySegment
from contacts.models import Contact


# Manager for serialization
class CustomerManager(models.Model):

    def get_by_natural_key(self, name):
        return self.get(name=name)


class Language(models.Model):
    objects = CustomerManager()
    name = models.CharField(max_length=25, unique=True)

    def natural_key(self):
        return self.name

    def __str__(self):
        return self.name


class ClientType(models.Model):
    objects = CustomerManager()
    name = models.CharField(max_length=50, unique=True)

    def natural_key(self):
        return self.name

    def __str__(self):
        return self.name


class Customer(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now=True)
    contact = models.ForeignKey(Contact,null=True)
    status = models.NullBooleanField(blank=True, null=True)
    language = models.ForeignKey(Language, blank=True,null=True)
    comment = models.TextField(blank=True, null=True)
    client_type = models.ForeignKey(ClientType, blank=True, null=True)
    discount_percent = models.FloatField(blank=True, null=True)
    company_segment = models.ForeignKey(CompanySegment, blank=True, null=True)

    def __str__(self):
        return self.name


class CustomerCategory(models.Model):
    objects = CustomerManager()
    name = models.CharField(max_length=50, unique=True)

    def natural_key(self, name=name):
        return self.name

    def __str__(self):
        return self.name


class CustomerGroup(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=100)
    customers = models.ManyToManyField(Customer)
    parent = models.ManyToManyField('self',symmetrical=False, blank=True, default='')
    category = models.ForeignKey(CustomerCategory, blank=True, null=True)

    def __str__(self):
        return self.name

        