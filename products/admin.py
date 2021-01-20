from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'category']
	search_fields = ['company_name']
		

# Register your models here.
admin.site.register(Product, ProductAdmin)
