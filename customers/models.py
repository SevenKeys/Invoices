from django.db import models
from companies.models import Company, CompanySegment
from contacts.models import Contact


class Customer(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now=True)
    contact = models.ForeignKey(Contact,null=True)
    status = models.NullBooleanField(blank=True,null=True)
    language = models.CharField(max_length=25,blank=True,null=True)
    comment = models.TextField(blank=True,null=True)
    client_type = models.CharField(max_length=25,blank=True,null=True)
    discount_percent = models.FloatField(blank=True,null=True)
    company_segment = models.ForeignKey(CompanySegment,blank=True,null=True)

    def __str__(self):
        return self.name


class CustomerGroup(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=100)
    customers = models.ManyToManyField(Customer)
    parent = models.ManyToManyField('self',symmetrical=False,blank=True,default='client_group')
    category = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.name

        