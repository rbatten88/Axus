from django.db import models
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
		('2pm-4pm', '2pm-4pm'), ('First Drop', 'First Drop'),
	)
	customer = models.ForeignKey(WholesaleCustomer, on_delete=models.CASCADE)
	transfer_type = models.CharField(max_length=8, choices=transfer_types, default='')
	transfer_date = models.DateField(null=True, blank=True)
	transfer_time = models.CharField(max_length=20, choices=transfer_times, default='')


	def __str__(self):
		return f"{self.id} - {self.customer}"

	def get_absolute_url(self):
		return reverse('order_list')

	class Meta(object):
		ordering = ['id']

class Item(models.Model):
	item = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField()
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')

	def __str__(self):
		return f"{self.order.id} - {self.item}"
 