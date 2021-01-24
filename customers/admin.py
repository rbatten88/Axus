from django.contrib import admin
from .models import WholesaleCustomer


class WholesaleCustomerAdmin(admin.ModelAdmin):
	list_display = ['name', 'phone_number']
	search_fields = ['name']
		

# Register your models here.
admin.site.register(WholesaleCustomer, WholesaleCustomerAdmin)
