from django.db import models
from companies.models import Company
from contacts.models import Contact


# class Customer(models.Model):
#     company = models.ForeignKey(Company)
#     name = models.CharField(max_length=60)
#     created = models.DateTimeField(auto_now=True)
#     contact = models.ForeignKey(Contact,null=True)

    # def __str__(self):
    #     return self.name

# languages = (
#     ('english','English'),
#     ('spanish','Spanish'),
#     ('russian','Russian'))
# types = (
#     ('retail','retail'),
#     ('wholesale','wholesale'),
#     ('dealer','dealer'))

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

    def __str__(self):
        return self.name

categories = (
    ('cat1','category1'),
    ('cat2','category2'),
    ('cat3','category3'))

class CustomerGroup(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=100)
    customers = models.ManyToManyField(Customer)
    parent = models.ManyToManyField('self',symmetrical=False,blank=True,default='client_group')
    category = models.CharField(max_length=100,choices=categories,blank=True,null=True)

    def __str__(self):
        return self.name

        