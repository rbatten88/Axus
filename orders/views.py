from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Order, Item
from .forms import OrderForm, ItemForm

# Create your views here.
def OrderCreateView(request):
    template = 'orders/order_add.html'
    if request.method == 'POST':
        order_form = OrderForm(request.POST, prefix='order')
        item_form = ItemForm(request.POST, prefix='item')
        if order_form.is_valid() and item_form.is_valid():
            Order = order_form.save()
            Item = item_form.save(commit=False)
            Item.order = Order
            Item.save()
            return redirect('order_list')

    # if a GET (or any other method) we'll create a blank form
    else:
        order_form = OrderForm(prefix='order')
        item_form = ItemForm(prefix='item')

    return render(request, template, {'order_form': order_form, 'item_form': item_form})


def OrderListView(request):
    template = 'orders/order_list.html'

    return render(request, template, {'orders': Order.objects.all()})

#class OrderListView(ListView):


class OrderUpdateView(UpdateView):
    model = Order
    context_object_name = 'order'
    template_name = 'orders/order_detail.html'


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('order_list')
		