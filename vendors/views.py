from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Vendor
from .forms import VendorForm

# Create your views here.
class VendorCreateView(CreateView):
	model = Vendor
	form_class = VendorForm
	template_name = 'vendors/vendor_add.html'


class VendorListView(ListView):
	model = Vendor
	context_object_name = 'vendors'
	template_name = 'vendors/vendor_list.html'


class VendorUpdateView(UpdateView):
	model = Vendor
	form_class = VendorForm
	template_name = 'vendors/vendor_detail.html'
	context_object_name = 'vendor'


class VendorDeleteView(DeleteView):
    model = Vendor
    success_url = reverse_lazy('vendor_list')
	