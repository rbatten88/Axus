from django.contrib import admin
from .models import Order, OrderItem, Load, LoadItem


class OrderAdmin(admin.ModelAdmin):
	list_display = ['id', 'customer', 'transfer_date', 'transfer_type']
	search_fields = ['id', 'customer']


class OrderItemAdmin(admin.ModelAdmin):
	list_display = ['item', 'order']
	search_fields = ['item']


class LoadAdmin(admin.ModelAdmin):
	list_display = ['temp_load_number', 'farm', 'transfer_date']
	search_fields = ['temp_load_number', 'farm']


class LoadItemAdmin(admin.ModelAdmin):
	list_display = ['item', 'quantity', 'load']
	search_fields = ['item']

# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Load, LoadAdmin)
admin.site.register(LoadItem, LoadItemAdmin)