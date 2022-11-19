from django.shortcuts import render,redirect
from accounts.models import Project
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from datetime import datetime,timedelta
from django.http.response import Http404,JsonResponse
from django.http import HttpResponse
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this

# Create your views here.

def index(request):
    return render(request, 'project_app/index.html',{'title':'index'})

def register_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful." )
            return redirect("login")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
            return render (request=request, template_name="project_app/register.html", context={"register_form":form})
    form = NewUserForm()
    return render (request=request, template_name="project_app/register.html", context={"register_form":form})


def login_user(request):
    return render(request,template_name="project_app/login.html")

def login_user(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="project_app/login.html", context={"login_form":form})

def home(request):
    return render(request,template_name="project_app/index.html")


