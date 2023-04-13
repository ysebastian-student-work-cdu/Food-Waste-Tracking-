from django.shortcuts import render
from . import items

# Create your views here.

# Core pages
def index(request):
    return render(request, 'users/index.html',{})

def list(request):
    return render(request, 'users/list.html',{})

#def detail(request):
#   return render(request, 'users/detail.html',{})

def data_model(request):
    return render(request, 'users/data_model.html',{})

# Details
def detail(request, id):
    if id == 'why-not-food-waste':
        context = {'item':items.reasons}
        page = 'users/details.html'
    elif id == 'resources':
        context = {'item':resources}

     # rest of items go here

    return render(request, page, context)


