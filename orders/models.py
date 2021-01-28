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
	#delivery_address = models.ForeignKey(DeliveryAddresses, on_delete=models.CASCADE)
	transfer_time = models.CharField(max_length=20, choices=transfer_times, default='')
	#delivery_assignment = models.ForeignKey(Logistics, on_delete=models.CASCADE)
	status_order = models.BooleanField(default=True)
	status_confirmed = models.BooleanField(default=False)
	status_inventory_assignment= models.BooleanField(default=False)
	status_invoice_made = models.BooleanField(default=False)
	status_out_for_delivery = models.BooleanField(default=False)
	status_delivered = models.BooleanField(default=False)
	status_invoice_paid= models.BooleanField(default=False)
	status_completed = models.BooleanField(default=False)
	entered_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	entered_on = models.DateField()
	last_modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	last_modified_on = models.DateField()


	def __str__(self):
		return f"{self.number} - {self.customer} - {self.tranfer_type}"

	def get_absolute_url(self):
		return reverse('order_list')

	class Meta(object):
		ordering = ['number']

class Transaction(models.Model):
	name = models.ForeignKey(Product, on_delete=models.CASCADE)
	number = models.ForeignKey(Order, on_delete=models.CASCADE)
	quantity = models.IntegerField()

	def __str__(self):
		return f"{self.number} - {self.name}"
 