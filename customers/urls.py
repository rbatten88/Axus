from django.urls import path

from . import views

urlpatterns = [
	path('add/', views.customer_add, name="customer_add"),
	path('list/', views.customer_list, name="customer_list"),
	path('detail/', views.customer_detail, name="customer_detail"),
	path('upload/', views.customer_upload, name="customer_upload"),
]
