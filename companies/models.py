from django.db import models
from contacts.models import Contact

class CompanyManager(models.Model):

    def get_by_natural_key(self, name):
        return self.get(name=name)

class Company(models.Model):
    name = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    contact = models.ForeignKey(Contact, blank=True, null=True)
    reg_code = models.CharField(max_length=30)
    credit_status = models.CharField(max_length=30,blank=True,null=True)
    office_number = models.IntegerField(blank=True,null=True)

    def __str__(self):
    	return self.name

class CompanySegment(models.Model):
    objects = CompanyManager()
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=60)

    def natural_key(self):
        return self.name

    def __str__(self):
        return self.name