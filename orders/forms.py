from django import forms
from django.forms import modelformset_factory
from .models import Order, OrderItem, Load, LoadItem

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
			'delivery_street': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
			'delivery_city': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
			'delivery_state': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
			'delivery_zip_code': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
			'order_notes': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
			'print_notes': forms.CheckboxInput(attrs={'tabindex': '-1'}),
		}


class OrderItemForm(forms.ModelForm):
	class Meta:
		model = OrderItem
		exclude = ['order']
		widgets = {
			'item': forms.Select(attrs={'class': 'form-control item', 'style': 'margin-bottom: 10px;', 'onchange' : 'itemChange(this);'}),
			'quantity': forms.NumberInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
		}


OrderItemFormSet = modelformset_factory(OrderItem, form=OrderItemForm, extra=1, can_delete=True)


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
			'delivery_street': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
			'delivery_city': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
			'delivery_state': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
			'delivery_zip_code': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
			'order_notes': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;', 'readonly': 'true'}),
			'print_notes': forms.CheckboxInput(attrs={'tabindex': '-1', 'disabled': ''}),
		}


class OrderItemEditForm(forms.ModelForm):
	class Meta:
		model = OrderItem
		fields = ['item', 'quantity', 'order']
		widgets = {
			'item': forms.Select(attrs={'class': 'form-control item', 'style': 'margin-bottom: 10px;', 'onchange' : 'itemChange(this);', 'disabled': ''}),
			'quantity': forms.NumberInput(attrs={'class': 'form-control quantity', 'style': 'margin-bottom: 10px;', 'readonly': 'true'}),
		}
		

OrderItemEditFormSet = modelformset_factory(OrderItem, form=OrderItemEditForm, extra=0, can_delete=True)


class LoadForm(forms.ModelForm):
	class Meta:
		model = Load
		exclude = ['temp_load_number', 'created_by', 'created_on', 'updated_by', 'updated_on']
		widgets = {
			'inv_number': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
			'farm': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;', 'autofocus': 'true'}),
			'cut_date': forms.DateInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;', 'autocomplete': 'off'}),
			'transfer_type': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
			'transfer_date': forms.DateInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;', 'autocomplete': 'off'}),
			'transfer_time': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
		}


class LoadItemForm(forms.ModelForm):
	class Meta:
		model = LoadItem
		exclude = ['load']
		widgets = {
			'item': forms.Select(attrs={'class': 'form-control item', 'style': 'margin-bottom: 10px;', 'onchange' : 'itemChange(this);'}),
			'quantity': forms.NumberInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
		}


LoadItemFormSet = modelformset_factory(LoadItem, form=LoadItemForm, extra=1, can_delete=True)


class LoadEditForm(forms.ModelForm):
	class Meta:
		model = Load
		exclude = ['created_by', 'created_on', 'updated_by', 'updated_on']
		widgets = {
			'temp_load_number': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;', 'readonly': 'true'}),
			'inv_number': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;', 'readonly': 'true'}),
			'farm': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;', 'autofocus': 'true', 'disabled': ''}),
			'cut_date': forms.DateInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;', 'autocomplete': 'off', 'disabled': ''}),
			'transfer_type': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;', 'disabled': ''}),
			'transfer_date': forms.DateInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;', 'autocomplete': 'off', 'disabled': ''}),
			'transfer_time': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;', 'disabled': ''}),
		}


class LoadItemEditForm(forms.ModelForm):
	class Meta:
		model = LoadItem
		fields = ['item', 'quantity', 'load']
		widgets = {
			'item': forms.Select(attrs={'class': 'form-control item', 'style': 'margin-bottom: 10px;', 'onchange' : 'itemChange(this);', 'disabled': ''}),
			'quantity': forms.NumberInput(attrs={'class': 'form-control quantity', 'style': 'margin-bottom: 10px;', 'readonly': 'true'}),
		}
		

LoadItemEditFormSet = modelformset_factory(LoadItem, form=LoadItemEditForm, extra=0, can_delete=True)