from django.db import models

# Create your models here.
class StorageManager(models.Manager):

	def get_by_natural_key(self, name):
		return self.get(name=name)


class StorageGroup(models.Model):
	objects = StorageManager()
	name = models.CharField(max_length=25, unique=True)

	def natural_key(self):
		return self.name

	def __str__(self):
		return self.name


class Storage(models.Model):
	name = models.CharField(max_length=25, unique=True)
	code = models.CharField(max_length=50, unique=True)
	description = models.TextField()
	group = models.ForeignKey(StorageGroup, blank=True, default='')
	max_number = models.IntegerField()

	def __str__(self):
		return self.name