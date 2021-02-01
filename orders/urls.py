from django.urls import path
from . import views

# Create your urls here.
urlpatterns = [
	path('add/', views.OrderCreateView, name='order_add'),
	path('list/', views.OrderListView.as_view(), name="order_list"),
	path('detail/<int:pk>', views.OrderUpdateView.as_view(), name="order_detail"),
	path('delete/<int:pk>', views.OrderDeleteView.as_view(), name="order_delete"),
]
