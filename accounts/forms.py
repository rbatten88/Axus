from django import forms
from .models import Account

class AccountForm(forms.ModelForm):
	class Meta:
		model = Account
		fields = '__all__'
		widgets = {
			'name': forms.TextInput(attrs={'autofocus': 'true', 'class': 'form-control'}),
			'description': forms.TextInput(attrs={'class': 'form-control'}),
		} 
