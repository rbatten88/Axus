from django.urls import path
from . import views

urlpatterns = [
	path('add/', views.AccountCreateView.as_view(), name='account_add'),
	path('list/', views.AccountListView.as_view(), name="account_list"),
	path('detail/<int:pk>', views.AccountUpdateView.as_view(), name="account_detail"),
	path('delete/<int:pk>', views.AccountDeleteView.as_view(), name="account_delete"),
]
 