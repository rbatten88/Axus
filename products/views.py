from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm

# Create your views here.
class ProductCreateView(CreateView):
	model = Product
	form_class = ProductForm
	template_name = 'products/product_add.html'


class ProductListView(ListView):
	model = Product
	context_object_name = 'products'
	template_name = 'products/product_list.html'


class ProductUpdateView(UpdateView):
	model = Product
	form_class = ProductForm
	template_name = 'products/product_detail.html'
	context_object_name = 'product'


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')
	