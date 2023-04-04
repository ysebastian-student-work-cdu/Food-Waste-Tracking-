from django.shortcuts import render

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
def reasons(request):
	return render(request, 'users/reasons.html')
