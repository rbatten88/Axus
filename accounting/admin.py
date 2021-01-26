from django.contrib import admin
from .models import Accounting


class AccountingAdmin(admin.ModelAdmin):
	list_display = ['name', 'description']
	search_fields = ['name']
		

# Register your models here.
admin.site.register(Accounting, AccountingAdmin)
