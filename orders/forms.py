from django import forms
from .models import Order, Item

# Create your forms here.
class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = '__all__'
		widgets = {
			'number': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
			'customer': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
			'transfer_type': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
			'transfer_date': forms.DateInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
			'transfer_time': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
		}


class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ['name', 'quantity']
		widgets = {
			'name': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
			'quantity': forms.NumberInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
		}

