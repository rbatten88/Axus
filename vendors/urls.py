from django.urls import path
from . import views

urlpatterns = [
	path('add/', views.VendorCreateView.as_view(), name='vendor_add'),
	path('list/', views.VendorListView.as_view(), name="vendor_list"),
	path('detail/<int:pk>', views.VendorUpdateView.as_view(), name="vendor_detail"),
	path('delete/<int:pk>', views.VendorDeleteView.as_view(), name="vendor_delete"),
]
 