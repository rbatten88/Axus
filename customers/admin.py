from django.contrib import admin
from .models import WholesaleCustomer, AdditionalEmail, AdditionalPhone


class WholesaleCustomerAdmin(admin.ModelAdmin):
	list_display = ['company_name', 'phone_number']
	search_fields = ['company_name']


class AdditionalPhoneAdmin(admin.ModelAdmin):
	list_display = ['company_name', 'phone_number']
	search_fields = ['company_name']


class AdditionalEmailAdmin(admin.ModelAdmin):
	list_display = ['company_name', 'email']
	search_fields = ['company_name']
		

# Register your models here.
admin.site.register(WholesaleCustomer, WholesaleCustomerAdmin)
admin.site.register(AdditionalEmail, AdditionalEmailAdmin)
admin.site.register(AdditionalPhone, AdditionalPhoneAdmin)
