from django.shortcuts import render, reverse, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.urls import reverse_lazy
from .models import WholesaleCustomer
from .forms import WholesaleCustomerForm, WholesaleCustomerEditForm
from customers.functions.functions import upload_attachment
import csv, io

# Create your views here.
@permission_required('admin.can_add_log_entry')
def customer_upload(request):
	template = 'customers/customer_upload.html'
	prompt = {
		'order': '''Order of csv should be Customer: Name, Phone Number, Email, Contact, Street, City, State, Zipcode, 2nd Phone Number, 3rd Phone Number, 2nd Email, 3rd Email'''
	}
	if request.method == "GET":
		return render(request, template, prompt)
	csv_file = request.FILES['filename']
	if not csv_file.name.endswith('.csv'):
		messages.error(request, 'This is not a csv file')
	data_set = csv_file.read().decode('UTF-8')
	io_string = io.StringIO(data_set)
	next(io_string)
	customer_list = csv.reader(io_string, delimiter=',', quotechar='"')
	for column in customer_list:
		if not column[2] == "":
			email_match = WholesaleCustomer.objects.filter(email=column[3]).first()
			if email_match == None:
				if column[8] == "":
					additional_phone = False
				else:
					additional_phone = True
					phone_number2 = column[8]
				if column[9] == "":
					additional_email = False
					email2 = ''
				else:
					additional_email = True
					email2 = column[9]
				if column[10] == "":
					additional_email2 = False
					email3 = ''
				else:
					additional_email2 = True
					email3 = column[10]
				wholesale_customer_created = WholesaleCustomer.objects.update_or_create(
					name=column[0],
					phone_number=column[1],
					invoice_static=column[3],
					street=column[4],
					city=column[5],
					state=column[6],
					zip_code=column[7],
					print_same=True,
					print_name=column[0],
					additional_phone=additional_phone,
					phone_number2=phone_number2,
					additional_email=additional_email,
					email2=email2,
					additional_email2=additional_email2,
					email3=email3,
				)
				'''
				customer = WholesaleCustomer.objects.latest('id')
				additional_phone_created = WCAdditionalPhone.objects.update_or_create(
						name=customer,
						phone_number=column[1],
				)
				if additional_phone == True:
					additional_phone_created = WCAdditionalPhone.objects.update_or_create(
						name=customer,
						phone_number=column[8],
					)
				if not column[2] == "":
					additional_email_created = WCAdditionalEmail.objects.update_or_create(
						name=customer,
						email=column[2],
					)
					if additional_email == True:
						additional_email_created = WCAdditionalEmail.objects.update_or_create(
							name=customer,
							email=column[9],
						)
					if additional_email2 == True:
						additional_email_created = WCAdditionalEmail.objects.update_or_create(
							name=customer,
							email=column[10],
						)'''
	return redirect(reverse('customer_list'))

'''
def WholesaleCustomerCreateView(request):
	if request.method == 'POST':
		customer_form = WholesaleCustomerForm(request.POST)
		email_form2 = WCAdditionalEmailForm(request.POST, prefix='email2')
		email_form3 = WCAdditionalEmailForm(request.POST, prefix='email3')
		if customer_form.is_valid() and email_form2.is_valid() and email_form3.is_valid():
			WholesaleCustomer = customer_form.save()
			WCAdditionalEmail = email_form2.save(commit=False)
			WCAdditionalEmail.name = WholesaleCustomer
			WCAdditionalEmail.save()
			WCAdditionalEmail = email_form3.save(commit=False)
			WCAdditionalEmail.name = WholesaleCustomer
			WCAdditionalEmail.save()
			return redirect('customer_list')
	else:
		customer_form = WholesaleCustomerForm()
		email_form2 = WCAdditionalEmailForm(prefix='email2')
		email_form3 = WCAdditionalEmailForm(prefix='email3')
	context = {
		'customer_form': customer_form,
		'email_form2': email_form2,
		'email_form3': email_form3,
	}
	return render(request, 'customers/customer_create.html', context)'''


class WholesaleCustomerCreateView(CreateView):
    model = WholesaleCustomer
    form_class = WholesaleCustomerForm
    context_object_name = 'customer'
    template_name = 'customers/customer_add.html'


class WholesaleCustomerListView(ListView):
    model = WholesaleCustomer
    context_object_name = 'customers'
    template_name = 'customers/customer_list.html'


class WholesaleCustomerUpdateView(UpdateView):
    model = WholesaleCustomer
    form_class = WholesaleCustomerEditForm
    context_object_name = 'customer'
    template_name = 'customers/customer_detail.html'


class WholesaleCustomerDeleteView(DeleteView):
    model = WholesaleCustomer
    success_url = reverse_lazy('customer_list')
