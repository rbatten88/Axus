from django.contrib import admin
from .models import Order, Item


class OrderAdmin(admin.ModelAdmin):
	list_display = ['id', 'customer', 'transfer_type']
	search_fields = ['id', 'customer']


class ItemAdmin(admin.ModelAdmin):
	list_display = ['item', 'order']
	search_fields = ['item']

# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(Item, ItemAdmin)