from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import CreateUserFrom
from django.contrib.auth import views
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth

# Create your views here.

def signup(request) :
    if request.method == "POST" :
        userform = CreateUserFrom(request.POST)
        if userform.is_valid() :
            userfrom.save()
            return redirect('home')
    elif request.method == 'GET' :
        userform = CreateUserFrom()

    return render(request, 'registration/signup.html', {'userform':userform})