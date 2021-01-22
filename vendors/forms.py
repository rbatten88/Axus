from django import forms
from .models import Vendor

class VendorForm(forms.ModelForm):
	class Meta:
		model = Vendor
		fields = '__all__'
		widgets = {
			'name': forms.TextInput(attrs={'autofocus': 'true', 'class': 'form-control'}),
			'category': forms.Select(attrs={'class': 'form-control', 'style': 'margin-bottom: 10px;'}),
		} 
