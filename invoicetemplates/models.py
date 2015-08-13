from django.db import models
from companies.models import Company


class Archetype(models.Model):
    company = models.ForeignKey(Company, blank=True, null=True)
    title = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ArchetypeElement(models.Model):
    code = models.CharField(max_length=30, unique=True)

    def __str__(self):
        if self.code:
            name = self.code
        else:
            name = '-'
        return name


class ArchetypeField(models.Model):
    archetype = models.ForeignKey(Archetype)
    element = models.ForeignKey(ArchetypeElement, null=True, blank=True)
    value = models.CharField(max_length=50)
    field = models.CharField(max_length=50, default="field")

    def __str__(self):
        return self.field + " " + self.archetype.title


class Template(models.Model):
    company = models.ForeignKey(Company)
    title = models.CharField(max_length=150)
    archetype = models.ForeignKey(Archetype, null=True, blank=True)
    description = models.CharField(max_length=300, default="")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class Component(models.Model):
    company = models.ForeignKey(Company, blank=True, null=True)
    default = models.BooleanField(default=False)
    removable = models.BooleanField(default=True)
    title = models.CharField(max_length=40)
    size_x = models.IntegerField()
    size_y = models.IntegerField()
    type = models.CharField(max_length=10, default="custom")
    content = models.CharField(max_length=3000, default="")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class ComponentInstance(models.Model):
    component = models.ForeignKey(Component)
    template = models.ForeignKey(Template, related_name='component_instances')
    reference = models.CharField(max_length=200, default="")
    position_x = models.IntegerField()
    position_y = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.component.title+'_'+self.invoiceTemplate.title

    def __str__(self):
        return str(self.position_x) + " " + str(self.position_y)


