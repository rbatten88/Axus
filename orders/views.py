from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from django.views.generic.edit import FormMixin, ProcessFormView
from django.urls import reverse_lazy
from django.forms import modelformset_factory
from .forms import OrderForm, ItemFormSet, OrderEditForm, ItemEditFormSet
from .models import Order, Item, Product


def OrderCreateView(request):
    template = 'orders/order_add.html'
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        item_form = ItemFormSet(request.POST)
        if order_form.is_valid() and item_form.is_valid():
            ordr = order_form.save(commit=False)
            ordr.created_by = request.user
            ordr.updated_by = request.user
            ordr = order_form.save()
            instances = item_form.save(commit=False)
            for instance in instances:
                instance.order = ordr
                instance.save()
            return redirect('order_list')

    else:
        order_form = OrderForm()
        item_form = ItemFormSet(queryset=Item.objects.none())

    return render(request, template, {'order_form': order_form, 'item_form': item_form})


def OrderListView(request):
    template = 'orders/order_list.html'
    orders = Order.objects.all()
    items = Item.objects.all()

    return render(request, template, {'orders': orders, 'items': items})


def OrderUpdateView(request, pk):
    template = 'orders/order_detail.html'
    order = get_object_or_404(Order, id=pk)
    products = Product.objects.all()
    created_by = order.created_by
    order_form = OrderEditForm(instance=order)
    item_form = ItemEditFormSet(queryset=Item.objects.filter(order_id=pk))
    if request.method == 'POST' :
        order_form = OrderEditForm(request.POST, instance=order)
        item_form = ItemEditFormSet(request.POST)
        if order_form.is_valid() and item_form.is_valid():
            ordr = order_form.save(commit=False)
            ordr.created_by = created_by
            ordr.updated_by = request.user
            order_form.save()
            item_form.save()
            return redirect('order_list')

    return render(request, template, {'order_form': order_form, 'item_form': item_form, 'order': order, 'products': products})

class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('order_list')
		