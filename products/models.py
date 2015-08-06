from django.db import models
from companies.models import Company

# cur = (
# 	('usd','USD'),
# 	('eur','EUR'),
# 	('rub','RUB'))
# categories = (
# 	('service','service'),
# 	('item','item'))
# units = (
# 	('unit1','unit1'),
# 	('unit2','unit2'),
# 	('unit3','unit3'))
# taxes = (
# 	(2,'2'),
# 	(4,'4'),
# 	(6,'6'))


class Product(models.Model):
    company = models.ForeignKey(Company)
    code = models.CharField(max_length=100,blank=True,null=True)
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    description = models.TextField(blank=True,null=True)
    # group = models.CharField(max_length=100,blank=True,default='')
    currency = models.CharField(max_length=25,blank=True,null=True)
    category = models.CharField(max_length=25,default='service')
    stock = models.IntegerField(blank=True,null=True)
    units_of_measure = models.CharField(max_length=25,default='unit1')
    # id_code = models.IntegerField()
    tax = models.IntegerField(default=2)
    price_with_tax = models.FloatField(default=0.0)

    def __str__(self):
    	return self.name

categs = (
	('categ1','category1'),
	('categ2','category2'),
	('categ3','category3'))

class ProductGroup(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=100)
    products = models.ManyToManyField(Product)
    parent = models.ManyToManyField('self',symmetrical=False,blank=True,default='goods')
    # group_id = models.IntegerField()
    # parent_id = models.IntegerField()
    description = models.TextField(blank=True,null=True)
    category = models.CharField(max_length=100,choices=categs,blank=True,null=True)

    def __str__(self):
    	return self.name
