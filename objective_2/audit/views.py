from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here

def accounts(request):
	return render(request, 'audit/accounts.html')
