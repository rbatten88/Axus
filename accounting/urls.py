from django.urls import path
from . import views

urlpatterns = [
	path('add/', views.AccountingCreateView.as_view(), name='accounting_add'),
	path('list/', views.AccountingListView.as_view(), name="accounting_list"),
	path('detail/<int:pk>', views.AccountingUpdateView.as_view(), name="accounting_detail"),
	path('delete/<int:pk>', views.AccountingDeleteView.as_view(), name="accounting_delete"),
]
 