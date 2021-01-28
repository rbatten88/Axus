from django.contrib import admin
from .models import Order, Transaction


class OrderAdmin(admin.ModelAdmin):
	list_display = ['number', 'customer']
	search_fields = ['number', 'customer']


class TransactionAdmin(admin.ModelAdmin):
	#order = Order.odjects.get(pk=)
	list_display = ['name', 'number']
	search_fields = ['name', 'number']

# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(Transaction, TransactionAdmin)