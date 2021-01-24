from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Account
from .forms import AccountForm

# Create your views here.
class AccountCreateView(CreateView):
	model = Account
	form_class = AccountForm
	template_name = 'chart_of_accounts/account_add.html'


class AccountListView(ListView):
	model = Account
	context_object_name = 'Accounts'
	template_name = 'chart_of_accounts/account_list.html'


class AccountUpdateView(UpdateView):
	model = Account
	form_class = AccountForm
	template_name = 'chart_of_accounts/account_detail.html'
	context_object_name = 'Account'


class AccountDeleteView(DeleteView):
    model = Account
    success_url = reverse_lazy('account_list')
	