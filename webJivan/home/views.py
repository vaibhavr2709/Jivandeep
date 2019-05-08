from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

def index(request):
	return render(request, 'home/index.html')

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username} !')
			return redirect('index')
		else:
			return redirect('signup')
	else:
		form = UserCreationForm()
	return render(request, 'home/signup.html', {'form' : form})

def login(request):
	return HttpResponse("<p> udwejgfuewkv </p>")