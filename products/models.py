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
    stock = models.IntegerField(blank=True, null=True)
    tax = models.IntegerField(default=2)
    price_with_tax = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

class Currency(models.Model):
    product = models.ForeignKey(Product,blank=True,null=True)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Category(models.Model):
    product = models.ForeignKey(Product,blank=True,null=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Unit(models.Model):
    product = models.ForeignKey(Product,blank=True,null=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tax(models.Model):
    product = models.ForeignKey(Product,blank=True,null=True,related_name='product')
    value = models.IntegerField(default=0)

    def __str__(self):
        return str(self.value)

