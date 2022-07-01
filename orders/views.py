from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from django.views.generic.edit import FormMixin, ProcessFormView
from django.urls import reverse_lazy
from django.forms import modelformset_factory
from .forms import OrderForm, OrderItemFormSet, OrderEditForm, OrderItemEditFormSet, LoadForm, LoadItemFormSet, LoadEditForm, LoadItemEditForm, LoadItemEditFormSet
from .models import Order, OrderItem, Product, Load, LoadItem
from django.utils import timezone
import datetime
import os

def OrderCreateView(request):
    template = 'orders/order_add.html'
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        order_item_form = OrderItemFormSet(request.POST)
        if order_form.is_valid() and order_item_form.is_valid():
            ordr = order_form.save(commit=False)
            ordr.created_by = request.user
            ordr.updated_by = request.user
            ordr = order_form.save()
            instances = order_item_form.save(commit=False)
            for instance in instances:
                instance.order = ordr
                instance.save()
            return redirect('order_list')

    else:
        order_form = OrderForm()
        order_item_form = OrderItemFormSet(queryset=OrderItem.objects.none())

    return render(request, template, {'order_form': order_form, 'order_item_form': order_item_form})


def OrderListView(request):
    template = 'orders/order_list_tabs.html'
    orders = Order.objects.all()
    items = OrderItem.objects.all()
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
    sun_orders = Order.objects.filter(transfer_date=sun)
    sun_pickups = Order.objects.filter(transfer_date=sun, transfer_type='Pickup')
    sun_del = Order.objects.filter(transfer_date=sun, transfer_type='Delivery')
    sun_loads = Load.objects.filter(transfer_date=sun)
    mon_orders = Order.objects.filter(transfer_date=mon)
    mon_pickups = Order.objects.filter(transfer_date=mon, transfer_type='Pickup')
    mon_del = Order.objects.filter(transfer_date=mon, transfer_type='Delivery')
    mon_loads = Load.objects.filter(transfer_date=mon)
    tue_orders = Order.objects.filter(transfer_date=tue)
    tue_pickups = Order.objects.filter(transfer_date=tue, transfer_type='Pickup')
    tue_del = Order.objects.filter(transfer_date=tue, transfer_type='Delivery')
    tue_loads = Load.objects.filter(transfer_date=tue)
    wed_orders = Order.objects.filter(transfer_date=wed)
    wed_pickups = Order.objects.filter(transfer_date=wed, transfer_type='Pickup')
    wed_del = Order.objects.filter(transfer_date=wed, transfer_type='Delivery')
    wed_loads = Load.objects.filter(transfer_date=wed)
    thu_orders = Order.objects.filter(transfer_date=thu)
    thu_pickups = Order.objects.filter(transfer_date=thu, transfer_type='Pickup')
    thu_del = Order.objects.filter(transfer_date=thu, transfer_type='Delivery')
    thu_loads = Load.objects.filter(transfer_date=thu)
    fri_orders = Order.objects.filter(transfer_date=fri)
    fri_pickups = Order.objects.filter(transfer_date=fri, transfer_type='Pickup')
    fri_del = Order.objects.filter(transfer_date=fri, transfer_type='Delivery')
    fri_loads = Load.objects.filter(transfer_date=fri)
    sat_orders = Order.objects.filter(transfer_date=sat)
    sat_pickups = Order.objects.filter(transfer_date=sat, transfer_type='Pickup')
    sat_del = Order.objects.filter(transfer_date=sat, transfer_type='Delivery')
    sat_loads = Load.objects.filter(transfer_date=sat)
    current_week_orders = [sun_orders, mon_orders, tue_orders, wed_orders, thu_orders, fri_orders, sat_orders]
    current_week_pickups = [sun_pickups, mon_pickups, tue_pickups, wed_pickups, thu_pickups, fri_pickups, sat_pickups]
    current_week_del = [sun_del, mon_del, tue_del, wed_del, thu_del, fri_del, sat_del]
    current_week_loads = [sun_loads, mon_loads, tue_loads, wed_loads, thu_loads, fri_loads, sat_loads]
    today = today.strftime("%x")
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
        'today': today, 'current_week_orders': current_week_orders, 'current_week_pickups': current_week_pickups,
        'current_week_del': current_week_del, 'current_week_loads': current_week_loads})


def UpdateWeekOrders(request):
<<<<<<< HEAD
    nd = request.GET.get('new_date', None)
    new_date = datetime.datetime.strptime(nd, '%Y-%m-%d')
    if new_date.weekday() == 6:
        sun = new_date - datetime.timedelta(days = new_date.weekday()-6)
        mon = new_date - datetime.timedelta(days = new_date.weekday()-7)
        tue = new_date - datetime.timedelta(days = new_date.weekday()-8)
        wed = new_date - datetime.timedelta(days = new_date.weekday()-9)
        thu = new_date - datetime.timedelta(days = new_date.weekday()-10)
        fri = new_date - datetime.timedelta(days = new_date.weekday()-11)
        sat = new_date - datetime.timedelta(days = new_date.weekday()-12)
    else:
        sun = new_date - datetime.timedelta(days = new_date.weekday()+1)
        mon = new_date - datetime.timedelta(days = new_date.weekday())
        tue = new_date - datetime.timedelta(days = new_date.weekday()-1)
        wed = new_date - datetime.timedelta(days = new_date.weekday()-2)
        thu = new_date - datetime.timedelta(days = new_date.weekday()-3)
        fri = new_date - datetime.timedelta(days = new_date.weekday()-4)
        sat = new_date - datetime.timedelta(days = new_date.weekday()-5)
    sun_orders = Order.objects.filter(transfer_date=sun)
    sun_pickups = Order.objects.filter(transfer_date=sun, transfer_type='Pickup')
    sun_del = Order.objects.filter(transfer_date=sun, transfer_type='Delivery')
    sun_loads = Load.objects.filter(transfer_date=sun)
    mon_orders = Order.objects.filter(transfer_date=mon)
    mon_pickups = Order.objects.filter(transfer_date=mon, transfer_type='Pickup')
    mon_del = Order.objects.filter(transfer_date=mon, transfer_type='Delivery')
    mon_loads = Load.objects.filter(transfer_date=mon)
    tue_orders = Order.objects.filter(transfer_date=tue)
    tue_pickups = Order.objects.filter(transfer_date=tue, transfer_type='Pickup')
    tue_del = Order.objects.filter(transfer_date=tue, transfer_type='Delivery')
    tue_loads = Load.objects.filter(transfer_date=tue)
    wed_orders = Order.objects.filter(transfer_date=wed)
    wed_pickups = Order.objects.filter(transfer_date=wed, transfer_type='Pickup')
    wed_del = Order.objects.filter(transfer_date=wed, transfer_type='Delivery')
    wed_loads = Load.objects.filter(transfer_date=wed)
    thu_orders = Order.objects.filter(transfer_date=thu)
    thu_pickups = Order.objects.filter(transfer_date=thu, transfer_type='Pickup')
    thu_del = Order.objects.filter(transfer_date=thu, transfer_type='Delivery')
    thu_loads = Load.objects.filter(transfer_date=thu)
    fri_orders = Order.objects.filter(transfer_date=fri)
    fri_pickups = Order.objects.filter(transfer_date=fri, transfer_type='Pickup')
    fri_del = Order.objects.filter(transfer_date=fri, transfer_type='Delivery')
    fri_loads = Load.objects.filter(transfer_date=fri)
    sat_orders = Order.objects.filter(transfer_date=sat)
    sat_pickups = Order.objects.filter(transfer_date=sat, transfer_type='Pickup')
    sat_del = Order.objects.filter(transfer_date=sat, transfer_type='Delivery')
    sat_loads = Load.objects.filter(transfer_date=sat)
    current_week_orders = [sun_orders, mon_orders, tue_orders, wed_orders, thu_orders, fri_orders, sat_orders]
    current_week_pickups = [sun_pickups, mon_pickups, tue_pickups, wed_pickups, thu_pickups, fri_pickups, sat_pickups]
    current_week_del = [sun_del, mon_del, tue_del, wed_del, thu_del, fri_del, sat_del]
    current_week_loads = [sun_loads, mon_loads, tue_loads, wed_loads, thu_loads, fri_loads, sat_loads]
    today = new_date.strftime("%x")
    sun_date_formatted = sun.strftime("%x")
    mon_date_formatted = mon.strftime("%x")
    tue_date_formatted = tue.strftime("%x")
    wed_date_formatted = wed.strftime("%x")
    thu_date_formatted = thu.strftime("%x")
    fri_date_formatted = fri.strftime("%x")
    sat_date_formatted = sat.strftime("%x")
    current_week_dates = [sun_date_formatted, mon_date_formatted, tue_date_formatted, wed_date_formatted, 
        thu_date_formatted, fri_date_formatted, sat_date_formatted]
    data = {'current_week_dates': current_week_dates, 'today': new_date, 'current_week_orders': current_week_orders, 
        'current_week_pickups': current_week_pickups,'current_week_del': current_week_del, 
        'current_week_loads': current_week_loads}
    return JsonResponse(data)
=======
    print("HELLO")
    if request.is_ajax and request.method == "POST":
        form = new_date_form(request.POST)
        new_date = form.new_date

>>>>>>> 2888f3fae9bc923c364c2cbcfbb6afd6cfc74863


def OrderUpdateView(request, pk):
    template = 'orders/order_detail.html'
    order = get_object_or_404(Order, id=pk)
    products = Product.objects.all()
    created_by = order.created_by
    order_form = OrderEditForm(instance=order)
    item_form = OrderItemEditFormSet(queryset=OrderItem.objects.filter(order_id=pk))
    if request.method == 'POST' :
        order_form = OrderEditForm(request.POST, instance=order)
        item_form = OrderItemEditFormSet(request.POST)
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


def LoadCreateView(request):
    template = 'orders/load_add.html'
    if request.method == 'POST':
        load_order_form = LoadForm(request.POST)
        load_item_form = LoadItemFormSet(request.POST)
        if load_order_form.is_valid() and load_item_form.is_valid():
            ordr = load_order_form.save(commit=False)
            trans_date = ordr.transfer_date.strftime("%m%d%y")
            ordr.temp_load_number = str(ordr.farm) + '-TL-' + str(trans_date) + '-' + str(Load.objects.filter(transfer_date=ordr.transfer_date).count() + 1)
            ordr.created_by = request.user
            ordr.updated_by = request.user
            ordr = load_order_form.save()
            instances = load_item_form.save(commit=False)
            for instance in instances:
                instance.available = instance.quantity
                instance.load = ordr
                instance.save()
            return redirect('order_list')

    else:
        load_order_form = LoadForm()
        load_item_form = LoadItemFormSet(queryset=LoadItem.objects.none())

    return render(request, template, {'load_order_form': load_order_form, 'load_item_form': load_item_form})


def LoadListView(request):
    template = 'orders/load_list.html'
    loads = Load.objects.all()
    items = LoadItem.objects.all()

    return render(request, template, {'loads': loads, 'items': items})


def LoadUpdateView(request, pk):
    template = 'orders/load_detail.html'
    load = get_object_or_404(Load, id=pk)
    products = Product.objects.all()
    created_by = load.created_by
    load_order_form = LoadEditForm(instance=load)
    item_form = LoadItemEditFormSet(queryset=LoadItem.objects.filter(load_id=pk))
    if request.method == 'POST' :
        load_order_form = LoadEditForm(request.POST, instance=load)
        item_form = LoadItemEditFormSet(request.POST)
        if load_order_form.is_valid() and item_form.is_valid():
            lode = load_order_form.save(commit=False)
            lode.created_by = created_by
            lode.updated_by = request.user
            load_order_form.save()
            instances = item_form.save(commit=False)
            for instance in instances:
                instance.available = instance.quantity
                instance.save()
            return redirect('load_list')

    return render(request, template, {'load_order_form': load_order_form, 'item_form': item_form, 'load': load, 'products': products})


class LoadDeleteView(DeleteView):
    model = Load
    success_url = reverse_lazy('load_list')
