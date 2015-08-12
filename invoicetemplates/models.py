from django.db import models
from companies.models import Company


class InvoiceTemplate(models.Model):
    company = models.ForeignKey(Company)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300, default="")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class TemplateComponent(models.Model):
    company = models.ForeignKey(Company, blank=True, null=True)
    default = models.BooleanField(default=False)
    removable = models.BooleanField(default=True)
    title = models.CharField(max_length=40)
    size_x = models.IntegerField()
    size_y = models.IntegerField()
    type = models.CharField(max_length=10, default="custom")
    content = models.CharField(max_length=1000, default="")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class TemplateComponentInstance(models.Model):
    component = models.ForeignKey(TemplateComponent)
    template = models.ForeignKey(InvoiceTemplate, related_name='component_instances')
    reference = models.CharField(max_length=200, default="")
    position_x = models.IntegerField()
    position_y = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.component.title+'_'+self.invoiceTemplate.title

    def __str__(self):
        return str(self.position_x) + " " + str(self.position_y)
