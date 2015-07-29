from django.db import models
from companies.models import Company
from products.models import Product


class Invoice(models.Model):
    title = models.CharField(max_length=200)
    companyFrom = models.ForeignKey(Company)
    companyTo = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class InvoiceProduct(models.Model):
    invoice = models.ForeignKey(Invoice)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.product.name


class InvoiceComponent(models.Model):
    title = models.CharField(max_length=200)
    company = models.ForeignKey(Company)
    type = models.CharField(max_length=20)
    content = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class InvoiceTemplate(models.Model):
    company = models.ForeignKey(Company)
    title = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title


class TemplateComponent(models.Model):
    company = models.ForeignKey(Company)
    default = models.BooleanField(default=False)
    title = models.CharField(max_length=40)
    size_x = models.IntegerField()
    size_y = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class TemplateComponentInstance(models.Model):
    component = models.ForeignKey(TemplateComponent)
    template = models.ForeignKey(InvoiceTemplate)
    position_x = models.IntegerField()
    position_y = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.component.title+'_'+self.invoiceTemplate.title
