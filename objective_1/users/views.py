from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from . import items

def index(request):
    return HttpResponse(loader.get_template('users/index.html').render())

def data_model(request):
    return HttpResponse(loader.get_template('users/data_model.html').render())


# Old Item Pages (We should delete the commented out section)

#def facts(request):
 #   return HttpResponse(loader.get_template('users/facts.html').render())

def reasons(request):
    return HttpResponse(loader.get_template('users/reasons.html').render())

#def benefits(request):
 #   return HttpResponse(loader.get_template('users/benefits.html').render())

#def solutions(request):
 #   return HttpResponse(loader.get_template('users/solutions.html').render())

#def resources(request):
 #   return HttpResponse(loader.get_template('users/resources.html').render())

def calculator(request):
    return HttpResponse(loader.get_template('users/calculator.html').render())


# New function to handle item url lookup
# Details
def detail(request, id):
    try:
        context = {'item':items.Item_Class.find(id)}
        page = "users/{}.html".format(id)
    except:
        context = {}
        page = "users/notfound.html"

    page = 'users/details.html'
    return render(request, page, context)


