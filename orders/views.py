from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from django.views.generic.edit import FormMixin, ProcessFormView
from django.urls import reverse_lazy
from django.forms import modelformset_factory
from .forms import OrderForm, ItemFormSet, OrderEditForm, ItemEditFormSet
from .models import Order, Item, Product


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
            print(item_form.errors)
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
    created_by = order.created_by
    order_form = OrderEditForm(instance=order)
    item_form = ItemEditFormSet(queryset=Item.objects.filter(order_id=pk))
    if request.method == 'POST' :
        order_form = OrderEditForm(request.POST, instance=order)
        item_form = ItemEditFormSet(request.POST)
        if order_form.is_valid():
            ordr = order_form.save(commit=False)
            ordr.created_by = created_by
            ordr.updated_by = request.user
            print(item_form.errors)
            instances = item_form.save(commit=False)
            for instance in instances:
                return HttpResponse('item')
                i_cd = item_form.cleaned_data
                instance.item = i_cd['item']
                instance.quantity = i_cd['quantity']
                instance.order = order
                instance.save()
            order_form.save()
            return redirect('order_list')

    return render(request, template, {'order_form': order_form, 'item_form': item_form, 'order': order})

'''
def OrderUpdateView(request, pk):
    template = 'orders/order_detail.html'
    order = get_object_or_404(Order, id=pk)
    #items = order.items.all()
    created_by = order.created_by
    if request.method == 'POST' :
        order_form = OrderEditForm(request.POST)
        item_form = ItemEditFormSet(request.POST)
        if order_form.is_valid():
            o_cd = order_form.cleaned_data
            order = order_form.save(commit=False)
            order.customer = o_cd['customer']
            order.transfer_type = o_cd['transfer_type']
            order.transfer_date = o_cd['transfer_date']
            order.transfer_time = o_cd['transfer_time']
            order.status = o_cd['status']
            order.delivery_street = o_cd['delivery_street']
            order.delivery_city = o_cd['delivery_city']
            order.delivery_state = o_cd['delivery_state']
            order.delivery_zip_code = o_cd['delivery_zip_code']
            order.order_notes = o_cd['order_notes']
            order.print_notes = o_cd['print_notes']
            order.created_by = created_by
            order.updated_by = request.user
            print(item_form.errors)
            instances = item_form.save(commit=False)
            for instance in instances:
                return HttpResponse('item')
                i_cd = item_form.cleaned_data
                instance.item = i_cd['item']
                instance.quantity = i_cd['quantity']
                instance.order = order
                instance.save()
            order.save()
            return redirect('order_list')
    else:
        order_form = OrderEditForm(instance=order)
        item_form = ItemEditFormSet(queryset=Item.objects.filter(order_id=pk))

    return render(request, template, {'order_form': order_form, 'item_form': item_form, 'order': order})

'''
class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('order_list')
		