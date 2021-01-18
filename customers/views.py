from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import permission_required
from django.urls import reverse, reverse_lazy
from .forms import WholesaleCustomerForm
from .models import WholesaleCustomer, AdditionalEmail, AdditionalPhone
from customers.functions.functions import upload_attachment
import csv, io

# Create your views here.
@permission_required('admin.can_add_log_entry')
def customer_upload(request):
	template = 'customers/customer_upload.html'
	prompt = {
		'order': 'Order of csv should be Customer Name, Phone Number, Email, Contact, Street, City, State, Zipcode'
	}
	if request.method == "GET":
		return render(request, template, prompt)
	csv_file = request.FILES['file']
	if not csv_file.name.endswith('.csv'):
		messages.error(request, 'This is not a csv file')
	data_set = csv_file.read().decode('UTF-8')
	io_string = io.StringIO(data_set)
	next(io_string)
	for column in csv.reader(io_string, delimiter=',', quotechar='"'):
		if not column[3] == "":
			email_match = WholesaleCustomer.objects.filter(email=column[3]).first()
			if email_match == None:
				if column[9] == "":
					additional_phone=False
				else:
					additional_phone=True
				if column[11] == "":
					additional_email=False
				else:
					additional_email=True
				_, wholesale_customer_created = WholesaleCustomer.objects.update_or_create(
					company_name=column[0],
					phone_number_type='m',
					phone_number=column[2],
					email=column[3],
					contact_name=column[4],
					street=column[5],
					city=column[6],
					state=column[7],
					zip_code=column[8],
					print_same=True,
					print_name=column[0],
					additional_phone=additional_phone,
					additional_email=additional_email,
				)
				if additional_phone == True:
					customer = WholesaleCustomer.objects.latest('id')
					if column[9] == 'office':
						phone_number_type = 'o'
					else:
						phone_number_type = 'm'
					_, additional_phone_created = AdditionalPhone.objects.update_or_create(
							company_name=customer,
							phone_number_type=phone_number_type,
							phone_number=column[10],
					)
				if additional_email == True:
					customer = WholesaleCustomer.objects.latest('id')
					_, additional_email_created = AdditionalEmail.objects.update_or_create(
							company_name=customer,
							email=column[11],
					)
					if not column[12] == '':
						_, additional_email_created = AdditionalEmail.objects.update_or_create(
							company_name=customer,
							email=column[12],
						)
	context = {}
	return render(request, template, context)


class WholesaleCustomerCreateView(CreateView):
    model = WholesaleCustomer
    form_class = WholesaleCustomerForm
    success_url = reverse_lazy('customer_list')
    template_name = 'customers/customer_add.html'


class WholesaleCustomerListView(ListView):
    model = WholesaleCustomer
    context_object_name = 'customers'
    template_name = 'customers/customer_list.html'


class WholesaleCustomerUpdateView(SuccessMessageMixin, UpdateView):
    model = WholesaleCustomer
    form_class = WholesaleCustomerForm
    template_name = 'customers/customer_detail.html'
    context_object_name = 'customer'
    success_url = reverse_lazy('customer_list')


class WholesaleCustomerDeleteView(DeleteView):
    model = WholesaleCustomer
    success_url = reverse_lazy('customer_list')
