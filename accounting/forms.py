from django import forms
from .models import Accounting

class AccountingForm(forms.ModelForm):
	class Meta:
		model = Accounting
		fields = '__all__'
		widgets = {
			'name': forms.TextInput(attrs={'autofocus': 'true', 'class': 'form-control'}),
			'description': forms.TextInput(attrs={'class': 'form-control'}),
		} 
