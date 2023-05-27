from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import *
from .forms import *

from . import utils

app_name = 'audit/'
# Create your views here

def index(request):
	return 0;



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
def donate(request):

    page_data = {'myform': DonationForm(), 'action': '/submit_donation' }

    return render(request, app_name + 'donate_create.html', page_data)

def submit_donation(request):
	# Add userID as default value before saving request.
	# id = request.session['id']
	# form = DonationForm(request.POST)
    # form(initial_value{'userID','request.session['id']})
	# Check if valid
	# save to db
	try:
		form = DonationForm(request['POST'])
		form(initial={'userID',"request.session['id']"})
	except(Exception):
		return 0
	if form.is_valid():
		form.save()
	else:
		return (request, my_app+'donate_create.html')

	

'''
Displays all donations made by user
'''
def donate_read(request):
	return 0

def accounts(request):
	return render(request, 'audit/accounts.html')
	
def waste_items_view(request, waste_entry_id):
    waste_items = utils.get_waste_items_by_entry_id(waste_entry_id)
    return render(request, 'audit/waste_items.html', {'waste_items': waste_items, 'waste_entry_id': waste_entry_id})
