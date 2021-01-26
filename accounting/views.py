from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Accounting
from .forms import AccountingForm

# Create your views here.
class AccountingCreateView(CreateView):
	model = Accounting
	form_class = AccountingForm
	template_name = 'accounting/accounting_add.html'


class AccountingListView(ListView):
	model = Accounting
	context_object_name = 'Accountings'
	template_name = 'accounting/accounting_list.html'


class AccountingUpdateView(UpdateView):
	model = Accounting
	form_class = AccountingForm
	template_name = 'accounting/accounting_detail.html'
	context_object_name = 'Accountings'


class AccountingDeleteView(DeleteView):
    model = Accounting
    success_url = reverse_lazy('accounting_list')
	