from django.contrib import admin
from .models import WholesaleCustomer


class WholesaleCustomerAdmin(admin.ModelAdmin):
	list_display = ['company_name', 'phone_number']
	search_fields = ['company_name']
		

# Register your models here.
admin.site.register(WholesaleCustomer, WholesaleCustomerAdmin)
