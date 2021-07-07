# apps/home/views.py

# Django modules
from django.shortcuts import render

# Django locals
from apps.home.models import Setting, ContactForm

# Create your views here.

# Homepage
def homepage(request):
	setting = Setting.objects.get(pk=1)
	page = 'homepage'
	context = {
		'setting':setting,
		'page':page,
	}
	return render(request, 'home/index.html', context)


# Aboutuspage
def aboutuspage(request):
	setting = Setting.objects.get(pk=1)
	page = 'aboutuspage'
	context = {
		'setting':setting,
		'page':aboutuspage,
	}	
	return render(request, 'home/about_us.html', context)


# Contactuspage
def contactuspage(request):
	setting = Setting.objects.get(pk=1)
	form = ContactForm
	# page = 'aboutuspage'
	context = {
		'setting':setting,
		'form':form,
		# 'page':aboutuspage,
	}	
	return render(request, 'home/contact_us.html', context)

