from django.db import models
from companies.models import Company

# class ProductCategory(models.Model):
#     name = models.CharField(max_length=50)

class ProductGroup(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=100)
    parent = models.ManyToManyField('self', symmetrical=False, blank=True, default='goods')
    description = models.TextField(blank=True, null=True)
    # category = models.ForeignKey(ProductCategory, blank=True, null=True)
    category = models.CharField(max_length=50,default='')

    def __str__(self):
        return self.name


class CurrencyManager(models.Manager):

    def get_by_natural_key(self,name):
        return self.get(name=name)


class Currency(models.Model):
    objects = CurrencyManager()
    name = models.CharField(max_length=25,unique=True)

    def natural_key(self):
        return self.name

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tax(models.Model):
    value = models.IntegerField(default=0)

    def __str__(self):
        return str(self.value)


class Product(models.Model):
    company = models.ForeignKey(Company)
    code = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    description = models.TextField(blank=True, null=True)
    group = models.ForeignKey(ProductGroup, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    currency = models.ForeignKey(Currency,default='')
    category = models.ForeignKey(Category,default='')
    unit = models.ForeignKey(Unit,default='')
    tax = models.ForeignKey(Tax,default=0)
    price_with_tax = models.FloatField(default=0.0)

    def __str__(self):
        return self.name



