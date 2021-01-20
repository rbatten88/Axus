from django.contrib import admin
from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return f"{self.name}"

	def get_absolute_url(self):
		return reverse('product_list')

	class Meta(object):
		ordering = ['name']