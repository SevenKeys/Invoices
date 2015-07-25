from django.db import models
from companies.models import Company


class Product(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=100)

    def __str__(self):
    	return self.name


class ProductGroup(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=100)
    products = models.ManyToManyField(Product)

    def __str__(self):
    	return self.name
