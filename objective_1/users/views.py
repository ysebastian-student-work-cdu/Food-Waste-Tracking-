from django.http import HttpResponse
from django.template import loader

def index(request):
    return HttpResponse(loader.get_template('index.html').render())

def facts(request):
    return HttpResponse(loader.get_template('facts.html').render())

def data_model(request):
    return HttpResponse(loader.get_template('data_model.html').render())

def reasons(request):
    return HttpResponse(loader.get_template('reasons.html').render())

def benefits(request):
    return HttpResponse(loader.get_template('benefits.html').render())

def solutions(request):
    return HttpResponse(loader.get_template('solutions.html').render())

def resources(request):
    return HttpResponse(loader.get_template('resources.html').render())

def calculator(request):
    return HttpResponse(loader.get_template('calculator.html').render())