# apps/home/views.py

# Django modules
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

# Django locals
from apps.home.models import Setting, ContactForm, ContactMessage

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
	if request.method == 'POST': # check post
		form = ContactForm(request.POST)
		if form.is_valid():
			data = ContactMessage() # create relation with model
			data.name = form.cleaned_data['name'] # get form input
			data.email = form.cleaned_data['email'] 
			data.subject = form.cleaned_data['subject'] 
			data.message = form.cleaned_data['message'] 
			data.ip = request.META.get('REMOTE_ADDR')
			data.save() # save data toble
			messages.success(request, "Your message hs been sent. Thank you for your message.")
			return HttpResponseRedirect('/contactus')

	setting = Setting.objects.get(pk=1)
	form = ContactForm
	context = {
		'setting':setting,
		'form':form,
	}	
	return render(request, 'home/contact_us.html', context)

