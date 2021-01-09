from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


# Create your views here.
def homepage(request):
	if request.user.is_authenticated:
		title = 'Home'
		return render(request, 'home/homepage.html', {'title': title})
	else:
		return redirect('/home/login/')
		