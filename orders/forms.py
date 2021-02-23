from django import forms
from django.forms import modelformset_factory
from .models import Order, Item

# Create your forms here.
class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		exclude = ['created_by', 'created_on', 'updated_by', 'updated_on']
		widgets = {
			'customer': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;', 'autofocus': 'true'}),
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
			'item': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;', 'onchange' : 'formReplicate();'}),
			'quantity': forms.NumberInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
		}


ItemFormSet = modelformset_factory(Item, form=ItemForm, extra=1, can_delete=True)


class OrderEditForm(forms.ModelForm):
	class Meta:
		model = Order
		exclude = ['created_by', 'created_on', 'updated_by', 'updated_on']
		widgets = {
			'customer': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;', 'autofocus': 'true', 'disabled': ''}),
			'transfer_type': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;', 'disabled': ''}),
			'transfer_date': forms.DateInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;', 'autocomplete': 'off', 'disabled': ''}),
			'transfer_time': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;', 'disabled': ''}),
			'status': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;', 'disabled': ''}),
		}


class ItemEditForm(forms.ModelForm):
	class Meta:
		model = Item
		exclude = ['order']
		widgets = {
			'item': forms.Select(attrs={'class': 'form-control item', 'style': 'margin-bottom: 10px;', 'onchange' : 'formReplicate():', 'disabled': ''}),
			'quantity': forms.NumberInput(attrs={'class': 'form-control quantity', 'style': 'margin-bottom: 10px;', 'readonly': 'true'}),
		}


ItemEditFormSet = modelformset_factory(Item, form=ItemEditForm, extra=0, can_delete=True)
