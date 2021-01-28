from django.shortcuts import render, reverse, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Order, Transaction
from .forms import OrderForm, OrderEditForm, TransactionForm

# Create your views here.
class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    context_object_name = 'order'
    template_name = 'orders/order_add.html'


class OrderListView(ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'orders/order_list.html'


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderEditForm
    context_object_name = 'order'
    template_name = 'orders/order_detail.html'


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('order_list')
		