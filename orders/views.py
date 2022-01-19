from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from django.views.generic.edit import FormMixin, ProcessFormView
from django.urls import reverse_lazy
from django.forms import modelformset_factory
from .forms import OrderForm, ItemFormSet, OrderEditForm, ItemEditFormSet
from .models import Order, Item, Product
from django.utils import timezone
import datetime
import os

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
    template = 'orders/order_list_tabs.html'
    orders = Order.objects.all()
    items = Item.objects.all()
    today = datetime.date.today()
    if today.weekday() == 6:
        sun = today - datetime.timedelta(days = today.weekday()-6)
        mon = today - datetime.timedelta(days = today.weekday()-7)
        tue = today - datetime.timedelta(days = today.weekday()-8)
        wed = today - datetime.timedelta(days = today.weekday()-9)
        thu = today - datetime.timedelta(days = today.weekday()-10)
        fri = today - datetime.timedelta(days = today.weekday()-11)
        sat = today - datetime.timedelta(days = today.weekday()-12)
    else:
        sun = today - datetime.timedelta(days = today.weekday()+1)
        mon = today - datetime.timedelta(days = today.weekday())
        tue = today - datetime.timedelta(days = today.weekday()-1)
        wed = today - datetime.timedelta(days = today.weekday()-2)
        thu = today - datetime.timedelta(days = today.weekday()-3)
        fri = today - datetime.timedelta(days = today.weekday()-4)
        sat = today - datetime.timedelta(days = today.weekday()-5)
    #current_week_ord = Order.objects.filter(transfer_date__gte=sun, transfer_date__lte=sat)
    #return HttpResponse(len(current_week_ord))
    sun_orders = Order.objects.filter(transfer_date=sun)
    mon_orders = Order.objects.filter(transfer_date=mon)
    tue_orders = Order.objects.filter(transfer_date=tue)
    wed_orders = Order.objects.filter(transfer_date=wed)
    thu_orders = Order.objects.filter(transfer_date=thu)
    fri_orders = Order.objects.filter(transfer_date=fri)
    sat_orders = Order.objects.filter(transfer_date=sat)
    current_week_orders = [sun_orders, mon_orders, tue_orders, wed_orders, thu_orders, fri_orders, sat_orders]
    #return HttpResponse(len(current_week_orders[4]))
    today = today.strftime("%x")
    #today_day = today.strftime("%A")
    #today = today_day + ' - ' + today_formatted
    sun_date_formatted = sun.strftime("%x")
    mon_date_formatted = mon.strftime("%x")
    tue_date_formatted = tue.strftime("%x")
    wed_date_formatted = wed.strftime("%x")
    thu_date_formatted = thu.strftime("%x")
    fri_date_formatted = fri.strftime("%x")
    sat_date_formatted = sat.strftime("%x")
    current_week_dates = [sun_date_formatted, mon_date_formatted, tue_date_formatted, wed_date_formatted, 
        thu_date_formatted, fri_date_formatted, sat_date_formatted]

    return render(request, template, {'orders': orders, 'items': items, 'current_week_dates': current_week_dates, 
        'today': today, 'current_week_orders': current_week_orders})


def UpdateWeekOrders(request):
    print("HELLO")
    if request.is_ajax and request.method == "POST":
        form = new_date_form(request.POST)
        new_date = form.new_date



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
		