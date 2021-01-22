from django.contrib import admin
from django.db import models
from django.urls import reverse

# Create your models here.
class Vendor(models.Model):
	categories = (
		('', ''), ('Farm', 'Farm'),
		('Pavers', 'Pavers'),
		('Compost', 'Compost'),
		('Other', 'Other'),
	)
	name = models.CharField(max_length=100, unique=True)
	category = models.CharField(max_length=100, choices=categories, default='')

	def __str__(self):
		return f"{self.name}"

	def get_absolute_url(self):
		return reverse('vendor_list')

	class Meta(object):
		ordering = ['name']
		