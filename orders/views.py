from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.forms import modelformset_factory
from .forms import OrderForm, ItemFormSet, OrderEditForm, ItemEditFormSet
from .models import Order, Item


# Create your views here.
'''
class OrderAddView(TemplateView):
    template_name = 'orders/order_add.html'

    def get(self, *args, **kwargs):
        order_form = OrderForm()
        item_form = ItemFormSet(queryset=Item.objects.none())
        return self.render_to_response({'order_form': order_form, 'item_form': item_form})

    def post(self, *args, **kwargs):
        order_form = OrderForm(data=self.request.POST)
        item_form = ItemFormSet(data=self.request.POST)
        if order_form.is_valid() and item_form.is_valid():
            order = order_form.save(commit=False)
            user = request.user
            order.created_by = user.username
            order.updated_by = user.username
            order.save()
            instances = item_form.save(commit=False)
            for instance in instances:
                instance.order = order
                instance.save()
            return redirect(reverse_lazy('order_list'))

        return self.render_to_response({'order_form': order_form, 'item_form': item_form})
'''

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
    items = order.items.all()
    if request.method == 'POST':
        order_form = OrderEditForm(request.POST)
        item_form = ItemEditFormSet(request.POST)
        if order_form.is_valid() and item_form.is_valid():
            return HttpResponse('HERE')
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
        order_form = OrderEditForm(instance=order)
        item_form = ItemEditFormSet(queryset=Item.objects.filter(order_id=pk))

    return render(request, template, {'order_form': order_form, 'item_form': item_form, 'order': order})


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('order_list')
		