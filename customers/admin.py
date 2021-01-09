from django.contrib import admin
from .models import WholesaleCustomer, AdditionalEmail, AdditionalPhone

# Register your models here.
admin.site.register(WholesaleCustomer)
admin.site.register(AdditionalEmail)
admin.site.register(AdditionalPhone)
