from django.db import models

# Create your models here.
number_type = (
		('m', 'Mobile'),
		('o', 'Office'),
	)
class WholesaleCustomer(models.Model):
	states = (
		('', ''),
		('nc', 'NC'),
		('sc', 'SC'),
		('va', 'VA'),
	)
	terms = (
		('', ''),
		('30', 'Net 30'),
		('60', 'Net 60'),
	)
	company_name = models.CharField(max_length=100, unique=True)
	contact_name = models.CharField(max_length=100, null=True, blank=True)
	phone_number_type = models.CharField(max_length=1, choices=number_type, default='m')
	phone_number = models.CharField(max_length=12, unique=True)
	additional_phone = models.BooleanField(default=False)
	email = models.EmailField(max_length=64, null=True, blank=True)
	additional_email = models.BooleanField(default=False)
	print_same = models.BooleanField(default=True)
	print_name = models.CharField(max_length=100)
	invoice_static = models.CharField(max_length=100, null=True, blank=True)
	street = models.CharField(max_length=100, null=True, blank=True)
	city = models.CharField(max_length=64, null=True, blank=True)
	state = models.CharField(max_length=2, null=True, blank=True, choices=states, default='')
	zip_code = models.CharField(max_length=10, null=True, blank=True)
	notes = models.TextField(max_length=254, null=True, blank=True)
	notes_popup = models.BooleanField(default=False)
	is_exempt = models.BooleanField(default=False)
	exemption_number = models.CharField(max_length=64, null=True, blank=True, unique=True)
	current_balance = models.IntegerField(default=0)
	has_credit = models.BooleanField(default=False)
	credit_limit = models.IntegerField(null=True, blank=True)
	credit_terms = models.CharField(max_length=2, null=True, blank=True, choices=terms, default='')
	opening_balance = models.IntegerField(null=True, blank=True)
	opening_balance_date = models.DateField(null=True, blank=True)
	has_attachments = models.BooleanField(default=False)
	is_inactive = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.company_name}"

	class Meta(object):
		ordering = ['company_name']


class AdditionalEmail(models.Model):
	company_name = models.ForeignKey(WholesaleCustomer, on_delete=models.CASCADE)
	email = models.EmailField(max_length=64, unique=True, null=True, blank=True)

	def __str__(self):
		return f"{self.company_name} - {self.email}"

	class Meta(object):
		ordering = ['company_name']


class AdditionalPhone(models.Model):
	company_name = models.ForeignKey(WholesaleCustomer, on_delete=models.CASCADE)
	phone_number_type = models.CharField(max_length=1, choices=number_type, default='o')
	phone_number = models.CharField(max_length=12, unique=True, null=True, blank=True)

	def __str__(self):
		return f"{self.company_name} - {self.phone_number}"

	class Meta(object):
		ordering = ['company_name']
		