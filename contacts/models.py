from django.db import models
from shared.utils import phone_regex


class Contact(models.Model):
    phone_number = models.CharField(max_length=16,
                                    validators=[phone_regex], blank=True)
    email = models.EmailField()
    street = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=60, blank=True)
    postcode = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=60)
    website = models.CharField(max_length=150, blank=True)

    def __str__(self):
    	return self.email

# Create your models here.
