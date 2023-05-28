from django.http import HttpResponse
from django.shortcuts import render

from . import views

def home(request):
    return render(request, 'users/index.html')

def facts(request):
    return render(request, 'users/facts.html')

def reasons(request):
    return render(request, 'users/reasons.html')

def solutions(request):
    return render(request, 'users/solutions.html')

def benefits(request):
    return render(request, 'users/benefits.html')

def data_model(request):
    return render(request, 'users/data_model.html')

def resources(request):
    return render(request, 'users/resources.html')

def login(request):
    return render(request, 'users/login.html')

def logout(request):
    return render(request, 'users/logout.html')

def wastelist(request):
    return render(request, 'users/wastelist.html')


