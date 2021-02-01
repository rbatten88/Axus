from django import forms
from .models import Order, Item

# Create your forms here.
class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		exclude = ['created_by', 'created_on', 'updated_by', 'updated_on']
		widgets = {
			'customer': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
			'transfer_type': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
			'transfer_date': forms.DateInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;', 'autocomplete': 'off'}),
			'transfer_time': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
			'status': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
		}


class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		exclude = ['order']
		widgets = {
			'item': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
			'quantity': forms.NumberInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
		}
