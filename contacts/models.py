from django.db import models
from shared.utils import phone_regex


class Contact(models.Model):
    phone_number = models.CharField(max_length=16,
                                    validators=[phone_regex], blank=True)
    email = models.EmailField()
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=60)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=60)
    website = models.CharField(max_length=150)

# Create your models here.
