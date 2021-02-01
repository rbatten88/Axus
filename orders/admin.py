from django.contrib import admin
from .models import Order, Item


class OrderAdmin(admin.ModelAdmin):
	list_display = ['number', 'customer']
	search_fields = ['number', 'customer']


class ItemAdmin(admin.ModelAdmin):
	#order = Order.odjects.get(pk=)
	list_display = ['name']
	search_fields = ['name']

# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(Item, ItemAdmin)