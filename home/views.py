from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomepageView(LoginRequiredMixin, TemplateView):
	login_url = 'home/login/'
	template_name = 'home/homepage.html'
	title = 'Home'
