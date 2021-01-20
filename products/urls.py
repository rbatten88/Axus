from django.urls import path
from . import views

urlpatterns = [
	path('add/', views.ProductCreateView.as_view(), name='product_add'),
	path('list/', views.ProductListView.as_view(), name="product_list"),
	path('detail/<int:pk>', views.ProductUpdateView.as_view(), name="product_detail"),
	path('delete/<int:pk>', views.ProductDeleteView.as_view(), name="product_delete"),
]
 