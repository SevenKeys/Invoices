from django.db import models
from companies.models import Company


class ProductGroup(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=100)
    parent = models.ManyToManyField('self', symmetrical=False, blank=True, default='goods')
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    company = models.ForeignKey(Company)
    code = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    description = models.TextField(blank=True, null=True)
    group = models.ForeignKey(ProductGroup, blank=True, null=True)
    currency = models.CharField(max_length=25, blank=True, null=True)
    category = models.CharField(max_length=25, default='service')
    stock = models.IntegerField(blank=True, null=True)
    units_of_measure = models.CharField(max_length=25, default='unit1')
    tax = models.IntegerField(default=2)
    price_with_tax = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
