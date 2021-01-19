from django.urls import path
from . import views

urlpatterns = [
	path('add/', views.WholesaleCustomerCreateView.as_view(), name='customer_add'),
	path('list/', views.WholesaleCustomerListView.as_view(), name="customer_list"),
	path('detail/<int:pk>', views.WholesaleCustomerUpdateView.as_view(), name="customer_detail"),
	path('delete/<int:pk>', views.WholesaleCustomerDeleteView.as_view(), name="customer_delete"),
	path('upload/', views.customer_upload, name="customer_upload"),
]
 