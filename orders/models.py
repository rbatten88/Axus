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
	number = models.IntegerField()
	customer = models.ForeignKey(WholesaleCustomer, on_delete=models.CASCADE)
	transfer_type = models.CharField(max_length=8, choices=transfer_types, default='')
	transfer_date = models.DateField(null=True, blank=True)
	transfer_time = models.CharField(max_length=20, choices=transfer_times, default='')


	def __str__(self):
		return f"{self.customer} - {self.transfer_type}"

	def get_absolute_url(self):
		return reverse('order_list')

	class Meta(object):
		ordering = ['number']

class Item(models.Model):
	name = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField()
	number = models.ForeignKey(Order, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.number} - {self.name}"
 