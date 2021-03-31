from django.urls import path
from . import views

# Create your urls here.
urlpatterns = [
	path('load_add/', views.LoadCreateView, name='load_add'),
	path('order_add/', views.OrderCreateView, name='order_add'),
	path('list/', views.OrderListView, name="order_list"),
	path('detail/<int:pk>', views.OrderUpdateView, name="order_detail"),
	path('delete/<int:pk>', views.OrderDeleteView.as_view(), name="order_delete"),
	path('update/', views.UpdateWeekOrders, name="update_week"),
	path('load_detail/<int:pk>', views.LoadUpdateView, name="load_detail"),
	path('load_delete/<int:pk>', views.LoadDeleteView.as_view(), name="load_delete"),
	path('load_list/', views.LoadListView, name="load_list"),
]
