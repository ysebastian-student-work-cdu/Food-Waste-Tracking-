from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html',{})

def list(request):
    return render(request, 'list.html',{})

def detail(request):
    return render(request, 'detail.html',{})

def data_model(request):
    return render(request, 'data_model.html',{})