from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import *
from .forms import *

from . import utils

# Create your views here

def accounts(request):
	return render(request, 'audit/accounts.html')

def waste_items_view(request, waste_entry_id):
    waste_items = utils.get_waste_items_by_entry_id(waste_entry_id)
    return render(request, 'audit/waste_items.html', {'waste_items': waste_items, 'waste_entry_id': waste_entry_id})