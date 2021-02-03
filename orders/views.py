from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import modelformset_factory
from .forms import OrderForm, ItemFormSet
from .models import Order, Item


# Create your views here.

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
    '''
    for order in orders:
        if order.items.count() > 1:
                order.transfer_type = 'TBD'
                '''
    return render(request, template, {'orders': orders})

'''
class OrderCreateView(CreateView):
    model = Order
    fields = ['customer', 'transfer_type', 'transfer_date', 'transfer_time', 'status']
    success_url = reverse_lazy('order_list')

    def get_context_data(self, **kwargs):
        data = super(OrderCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['items'] = ItemFormSet(self.request.POST)
        else:
            data['items'] = ItemFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        items = context['items']
        with transaction.atomic():
            self.object = form.save()

            if items.is_valid():
                items.instance = self.object
                items.save()
        return super(OrderCreateView, self).form_valid(form)'''


class OrderUpdateView(UpdateView):
    model = Order
    context_object_name = 'order'
    template_name = 'orders/order_detail.html'


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('order_list')
		