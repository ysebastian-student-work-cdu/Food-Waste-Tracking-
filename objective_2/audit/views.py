from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here

def index(request):
	return render(request, 'audit/index.html')

'''
Adds a new user to the user table
'''
def user_create(request):
	return 0
	
'''
Updates a user's password in the user table
'''
def user_update(request):
	return 0


'''
Deletes a user from the user table
'''
def user_delete(request):
	return 0


'''
Deletes a user from the user table
'''
def user_delete(request):
	return 0

'''
	Logs new entry into food audit table
'''
def log_create(request):
	return 0


'''
Displays all entries into food audit table by specific user
'''
def log_read(request):
	return 0

'''
	Adds a new donation by user to a food waste org to donation table
'''
def donate_create(request):

    page_data = {'myform': DonationForm(), }

    return render(request, app_name + 'donate_create.html', page_data)
	

'''
Displays all donations made by user
'''
def donate_read(request):
	return 0