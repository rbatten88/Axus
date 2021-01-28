from django import forms
from .models import Order, Transaction

# Create your forms here.
class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = '__all__'
		widgets = {
			'number': forms.HiddenInput(),
			'customer': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
			'transfer_type': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
			'transfer_date': forms.DateInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
			#delivery_address: forms.ForeignKey(DeliveryAddresses, on_delete=models.CASCADE)
			'transfer_time': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
			#delivery_assignment: forms.ForeignKey(Logistics, on_delete=models.CASCADE)
			'status_order': forms.CheckboxInput(attrs={'tabindex': '-1'}),
			'status_confirmed': forms.CheckboxInput(attrs={'tabindex': '-1'}),
			'status_inventory_assignment': forms.CheckboxInput(attrs={'tabindex': '-1'}),
			'status_invoice_made': forms.CheckboxInput(attrs={'tabindex': '-1'}),
			'status_out_for_delivery': forms.CheckboxInput(attrs={'tabindex': '-1'}),
			'status_delivered': forms.CheckboxInput(attrs={'tabindex': '-1'}),
			'status_invoice_paid': forms.CheckboxInput(attrs={'tabindex': '-1'}),
			'status_completed': forms.CheckboxInput(attrs={'tabindex': '-1'}),
			'entered_by': forms.HiddenInput(),
			'entered_on': forms.HiddenInput(),
			'last_modified_by': forms.HiddenInput(),
			'last_modified_on': forms.HiddenInput(),
		}
'''
	def __init__(self, *args, **kwargs):
		super(OrderForm, self).__init__(*args, **kwargs)
		self.fields['customer']=forms.ModelChoiceField(queryset=WholesaleCustomer.odjects.all())
'''

class OrderEditForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = '__all__'
		widgets = {}


class TransactionForm(forms.ModelForm):
	class Meta:
		model = Transaction
		fields = '__all__'
		widgets = {
			'item': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
			'number': forms.HiddenInput(),
			'quantity': forms.IntegerField(),
		}