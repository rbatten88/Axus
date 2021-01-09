from django import forms
from .models import WholesaleCustomer

class WholesaleCustomerForm(forms.ModelForm):
	class Meta:
		model = WholesaleCustomer
		fields = '__all__'
		widgets = {
			'company_name': forms.TextInput(attrs={'autofocus': 'true', 'class': 'form-control'}),
			'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
			'additional_phone': forms.CheckboxInput(attrs={'tabindex': '-1'}),
			'email': forms.EmailInput(attrs={'class': 'form-control'}),
			'additional_email': forms.CheckboxInput(attrs={'tabindex': '-1'}),
			'print_name': forms.TextInput(attrs={'class': 'form-control', 'tabindex': '-1', 'readonly': 'true'}),
			'print_same': forms.CheckboxInput(attrs={'tabindex': '-1'}),
			'street': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
			'city': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
			'state': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
			'zip_code': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
			'invoice_static': forms.TextInput(attrs={'class': 'form-control'}),
			'is_inactive': forms.CheckboxInput(attrs={'tabindex': '-1'}),
			'notes': forms.Textarea(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
			'exemption_number': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'true', 'style': 'margin-bottom: 10px;'}),
			'credit_limit': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'true', 'style': 'margin-bottom: 10px;'}),
			'credit_terms': forms.Select(attrs={'class': 'form-control', 'disabled': '', 'style': 'margin-bottom: 10px;'}),
			'opening_balance': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'true', 'style': 'margin-bottom: 10px;'}),
			'opening_balance_date': forms.DateInput(attrs={'class': 'form-control', 'disabled': '', 'style': 'margin-bottom: 10px;'}),
		} 
