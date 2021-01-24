from django.contrib import admin
from .models import Vendor


class VendorAdmin(admin.ModelAdmin):
	list_display = ['name', 'category']
	search_fields = ['name']
		

# Register your models here.
admin.site.register(Vendor, VendorAdmin)
