from django.contrib import admin
from .models import WholesaleCustomer, WCAdditionalEmail


class WholesaleCustomerAdmin(admin.ModelAdmin):
	list_display = ['name', 'phone_number']
	search_fields = ['name']
		

class WCAdditionalEmailAdmin(admin.ModelAdmin):
	list_display = ['name', 'email']
	search_fields = ['name']


# Register your models here.
admin.site.register(WholesaleCustomer, WholesaleCustomerAdmin)
admin.site.register(WCAdditionalEmail, WCAdditionalEmailAdmin)
