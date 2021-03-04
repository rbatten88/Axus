from django.db import models
from django.urls import reverse

# Create your models here.
class WholesaleCustomer(models.Model):
	'''
	customer_types = (
		('', ''), ('Retail', 'Retail'), ('Wholesale', 'Wholesale'),
	)'''
	states = (
		('', ''), ('NC', 'NC'), ('SC', 'SC'), ('VA', 'VA'), ('KY', 'KY'),
	)
	terms = (
		('', ''), ('Net 30', 'Net 30'), ('Net 60', 'Net 60'),
	)
	name = models.CharField(max_length=100, unique=True)
	#customer_type = models.CharField(max_length=9, choices=customer_types, default='')
	phone_number = models.CharField(max_length=12, unique=True)
	additional_phone = models.BooleanField(default=False)
	phone_number2 = models.CharField(max_length=12, null=True, blank=True)
	additional_phone2 = models.BooleanField(default=False)
	phone_number3 = models.CharField(max_length=12, null=True, blank=True)
	email = models.EmailField(max_length=64, null=True, blank=True)
	additional_email = models.BooleanField(default=False)
	email2 = models.EmailField(max_length=64, null=True, blank=True)
	additional_email2 = models.BooleanField(default=False)
	email3 = models.EmailField(max_length=64, null=True, blank=True)
	print_same = models.BooleanField(default=True)
	print_name = models.CharField(max_length=100)
	invoice_static = models.CharField(max_length=100, null=True, blank=True)
	street = models.CharField(max_length=100, null=True, blank=True)
	city = models.CharField(max_length=64, null=True, blank=True)
	state = models.CharField(max_length=2, null=True, blank=True, choices=states, default='NC')
	zip_code = models.CharField(max_length=10, null=True, blank=True)
	notes = models.TextField(max_length=254, null=True, blank=True)
	notes_popup = models.BooleanField(default=False)
	is_exempt = models.BooleanField(default=False)
	exemption_number = models.CharField(max_length=64, null=True, blank=True, unique=True)
	current_balance = models.IntegerField(default='0', null=True, blank=True)
	has_credit = models.BooleanField(default=False)
	credit_limit = models.IntegerField(null=True, blank=True)
	credit_terms = models.CharField(max_length=20, null=True, blank=True, choices=terms, default='')
	opening_balance = models.IntegerField(null=True, blank=True)
	opening_balance_date = models.DateField(null=True, blank=True)
	has_attachments = models.BooleanField(default=False)
	#attachments = models.FileField()
	is_inactive = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.name}"

	def get_absolute_url(self):
		return reverse('customer_list')

	class Meta(object):
		ordering = ['name']
		
'''
class WCAdditionalEmail(models.Model):
	name = models.ForeignKey(WholesaleCustomer, on_delete=models.CASCADE)
	email = models.EmailField(max_length=64, null=True, blank=True)

	def __str__(self):
		return f"{self.name}"

	class Meta(object):
		ordering = ['name']


class WCAdditionalPhone(models.Model):
	name = models.ForeignKey(WholesaleCustomer, on_delete=models.CASCADE)
	phone_number = models.CharField(max_length=12, unique=True)

	def __str__(self):
		return f"{self.name}"

	class Meta(object):
		ordering = ['name']'''
