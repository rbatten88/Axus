from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUser
	list_display = ['username', 'email', 'contact_number', 'location', 'access_level',]
	fieldsets = UserAdmin.fieldsets + (
		(None, {'fields': ('contact_number', 'location', 'access_level',)}),
	)
	add_fieldsets = UserAdmin.add_fieldsets + (
		(None, {'fields': ('contact_number', 'location', 'access_level',)}),
	)
		

# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)