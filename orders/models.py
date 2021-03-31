from django.db import models
from vendors.models import Vendor
from products.models import Product
from customers.models import WholesaleCustomer
from django.conf import settings

# Create your models here.
class Order(models.Model):
	transfer_types = (
		('', ''), ('Delivery', 'Delivery'), ('Pickup', 'Pickup'), ('TBD', 'TBD'),
	)
	transfer_times = (
		('', ''), ('AM', 'AM'), ('PM', 'PM'), ('Anytime', 'Anytime'), 
		('8am-10am', '8am-10am'), ('10am-12pm', '10am-12pm'), ('12pm-2pm', '12pm-2pm'), 
		('2pm-4pm', '2pm-4pm'), ('First Drop', 'First Drop'), ('Installing Tomorrow', 'Installing Tomorrow'),
	)
	states = (
		('', ''), ('NC', 'NC'), ('SC', 'SC'), ('VA', 'VA'), ('KY', 'KY'),
	)
	statuses = (
		('Order', 'Order'), ('Confirmed', 'Confirmed'), ('Load Matched', 'Load Matched'), ('Invoice Made', 'Invoice Made'),
		('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered'), ('Settled', 'Settled'), ('Completed', 'Completed'),
	)
	customer = models.ForeignKey(WholesaleCustomer, on_delete=models.CASCADE)
	transfer_type = models.CharField(max_length=8, choices=transfer_types, default='')
	transfer_date = models.DateField(null=True, blank=True)
	transfer_time = models.CharField(max_length=20, choices=transfer_times, default='')
	is_delivery = models.BooleanField(default=False)
	delivery_street = models.CharField(max_length=100, null=True, blank=True)
	delivery_city = models.CharField(max_length=64, null=True, blank=True)
	delivery_state = models.CharField(max_length=2, null=True, blank=True, choices=states, default='NC')
	delivery_zip_code = models.CharField(max_length=10, null=True, blank=True)
	order_notes = models.CharField(max_length=255, null=True, blank=True)
	print_notes = models.BooleanField(default=False)
	#delivery_assignment = models.ForeignKey(Logistics, on_delete=models.CASCADE)
	status = models.CharField(max_length=20, choices=statuses, default='Order')
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+', default='')
	created_on = models.DateTimeField(auto_now_add=True)
	updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	updated_on = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.id} - {self.customer}"

	def get_absolute_url(self):
		return reverse('order_list')

	class Meta(object):
		ordering = ['id']


class OrderItem(models.Model):
	item = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField()
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')


class Load(models.Model):
	transfer_types = (
		('', ''), ('Delivery', 'Delivery'), ('Pickup', 'Pickup'), ('TBD', 'TBD'),
	)
	transfer_times = (
		('', ''), ('Overnight', 'Overnight'), ('Morning', 'Morning'), ('Noon', 'Noon'), 
		('8am-10am', '8am-10am'), ('10am-12pm', '10am-12pm'), ('12pm-2pm', '12pm-2pm'), 
		('2pm-4pm', '2pm-4pm'),
	)
	temp_load_number = models.CharField(max_length=12)
	inv_number = models.CharField(max_length=20, null=True, blank=True)
	farm = models.ForeignKey(Vendor, on_delete=models.CASCADE, limit_choices_to={'category': 'Farm'})
	cut_date = models.DateField()
	transfer_date = models.DateField()
	transfer_type = models.CharField(max_length=8, choices=transfer_types, default='')
	transfer_time = models.CharField(max_length=9, choices=transfer_times, default='')
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+', default='')
	created_on = models.DateTimeField(auto_now_add=True)
	updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	updated_on = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.temp_load_number} - {self.farm} {self.transfer_date}"

	def get_absolute_url(self):
		return reverse('order_list')

	class Meta(object):
		ordering = ['temp_load_number']


class LoadItem(models.Model):
	item = models.ForeignKey(Product, on_delete=models.CASCADE, limit_choices_to={'category': 'Sod'})
	quantity = models.IntegerField()
	load = models.ForeignKey(Load, on_delete=models.CASCADE, related_name='items')
