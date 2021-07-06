# apps/home/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

def homepage(request):
	return render(request, 'home/index.html')


def aboutuspage(request):
	return render(request, 'home/about_us.html')


def contactuspage(request):
	return render(request, 'home/contact_us.html')