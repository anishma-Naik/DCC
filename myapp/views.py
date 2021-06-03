from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from myapp.models import Place
import django

# Create your views here.
from .models import *
from .forms import  CreateUserForm


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('/login')
			

		context = {'form':form}
		return render(request, 'myapp/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'myapp/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
def home(request):
	return render(request, 'myapp/base.html')


@login_required(login_url='login')
def beaches(request):
	beaches = Place.objects.filter(type='beach')
	context={
		'beaches' : beaches
	}
	return render(request,'myapp/beach.html',context)


@login_required(login_url='login')
def hillstations(request):
    return render(request, 'myapp/hill.html')

@login_required(login_url='login')
def heritagesites(request):
    return render(request, 'myapp/heritage.html')

def error_404_view(request, exception):
    data = {"name": "BOOK MY HOLIDAY"}
    return django.views.defaults.page_not_found(request, 'myapp/404_error.html')

