from django.db import models
from companies.models import Company
from products.models import Product


class Invoice(models.Model):
    title = models.CharField(max_length=200)
    companyFrom = models.ForeignKey(Company)
    companyTo = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class InvoiceProduct(models.Model):
    invoice = models.ForeignKey(Invoice)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name


class InvoiceComponent(models.Model):
    title = models.CharField(max_length=200)
    company = models.ForeignKey(Company)
    type = models.CharField(max_length=20)
    content = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class InvoiceTemplate(models.Model):
    company = models.ForeignKey(Company)
    title = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class InvoiceTemplateComponent(models.Model):
    component = models.ForeignKey(InvoiceComponent)
    invoiceTemplate = models.ForeignKey(InvoiceTemplate)
    position = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.component.title+'_'+self.invoiceTemplate.title
