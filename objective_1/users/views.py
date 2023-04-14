from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from . import items

def index(request):
    return HttpResponse(loader.get_template('users/index.html').render())

def facts(request):
    return HttpResponse(loader.get_template('users/facts.html').render())

def data_model(request):
    return HttpResponse(loader.get_template('users/data_model.html').render())

def reasons(request):
    return HttpResponse(loader.get_template('users/reasons.html').render())

def benefits(request):
    return HttpResponse(loader.get_template('users/benefits.html').render())

def solutions(request):
    return HttpResponse(loader.get_template('users/solutions.html').render())

def resources(request):
    return HttpResponse(loader.get_template('users/resources.html').render())

def calculator(request):
    return HttpResponse(loader.get_template('users/calculator.html').render())

# Details
def detail(request, id):
    if id == 'why-not-food-waste':
        context = {'item':items.reasons}
        page = 'users/details.html'
    elif id == 'resources':
        context = {'item':resources}

     # rest of items go here

    return render(request, page, context)
