from django import forms
from .models import WholesaleCustomer

class WholesaleCustomerForm(forms.ModelForm):
	class Meta:
		model = WholesaleCustomer
		fields = '__all__'
		widgets = {
			#'customer_type': forms.Select(attrs={'autofocus': 'true', 'class': 'form-control'}),
			'name': forms.TextInput(attrs={'autofocus': 'true', 'class': 'form-control'}),
			'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
			'additional_phone': forms.CheckboxInput(attrs={'tabindex': '-1'}),
			'phone_number2': forms.TextInput(attrs={'class': 'form-control'}),
			'additional_phone2': forms.CheckboxInput(attrs={'tabindex': '-1'}),
			'phone_number3': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.EmailInput(attrs={'class': 'form-control'}),
			'additional_email': forms.CheckboxInput(attrs={'tabindex': '-1'}),
			'email2': forms.EmailInput(attrs={'class': 'form-control'}),
			'additional_email2': forms.CheckboxInput(attrs={'tabindex': '-1'}),
			'email3': forms.EmailInput(attrs={'class': 'form-control'}),
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


class WholesaleCustomerEditForm(forms.ModelForm):
	class Meta:
		model = WholesaleCustomer
		fields = '__all__'
		widgets = {
			#'customer_type': forms.Select(attrs={'autofocus': 'true', 'class': 'form-control'}),
			'name': forms.TextInput(attrs={'autofocus': 'true', 'class': 'form-control', 'readonly': 'true'}),
			'phone_number': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'true'}),
			'additional_phone': forms.CheckboxInput(attrs={'tabindex': '-1', 'disabled': ''}),
			'phone_number2': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'true'}),
			'additional_phone2': forms.CheckboxInput(attrs={'tabindex': '-1', 'disabled': ''}),
			'phone_number3': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'true'}),
			'email': forms.EmailInput(attrs={'class': 'form-control', 'readonly': 'true'}),
			'additional_email': forms.CheckboxInput(attrs={'tabindex': '-1', 'disabled': ''}),
			'email2': forms.EmailInput(attrs={'class': 'form-control', 'readonly': 'true'}),
			'additional_email2': forms.CheckboxInput(attrs={'tabindex': '-1', 'disabled': ''}),
			'email3': forms.EmailInput(attrs={'class': 'form-control', 'readonly': 'true'}),
			'print_name': forms.TextInput(attrs={'class': 'form-control', 'tabindex': '-1', 'readonly': 'true'}),
			'print_same': forms.CheckboxInput(attrs={'tabindex': '-1', 'disabled': ''}),
			'street': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;', 'readonly': 'true'}),
			'city': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;', 'readonly': 'true'}),
			'state': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;', 'disabled': ''}),
			'zip_code': forms.TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;', 'readonly': 'true'}),
			'invoice_static': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'true'}),
			'is_inactive': forms.CheckboxInput(attrs={'tabindex': '-1', 'disabled': ''}),
			'notes_popup': forms.CheckboxInput(attrs={'tabindex': '-1', 'disabled': ''}),
			'notes': forms.Textarea(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;', 'readonly': 'true'}),
			'is_exempt': forms.CheckboxInput(attrs={'tabindex': '-1', 'disabled': ''}),
			'exemption_number': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'true', 'style': 'margin-bottom: 10px;'}),
			'has_credit': forms.CheckboxInput(attrs={'tabindex': '-1', 'disabled': ''}),
			'credit_limit': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'true', 'style': 'margin-bottom: 10px;'}),
			'credit_terms': forms.Select(attrs={'class': 'form-control', 'disabled': '', 'style': 'margin-bottom: 10px;'}),
			'opening_balance': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'true', 'style': 'margin-bottom: 10px;'}),
			'opening_balance_date': forms.DateInput(attrs={'class': 'form-control', 'disabled': '', 'style': 'margin-bottom: 10px;'}),
		} 
'''
class WCAdditionalEmailForm(forms.ModelForm):
	class Meta:
		model = WCAdditionalEmail
		fields = ['email']
		widgets = {
			'email': forms.EmailInput(attrs={'class': 'form-control'}),
		}'''
