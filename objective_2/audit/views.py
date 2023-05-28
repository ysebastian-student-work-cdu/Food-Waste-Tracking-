from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import *
from .forms import *
from .recipe import *

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
	request.session['id'] = '443'
	form = DonationForm(initial={'userID':f"{request.session['id']}"})
	page_data = {'myform': form, 'action': '/submit_donation'}

	return render(request, app_name + 'donate_create.html', page_data)

def submit_donation(request):
	# Add userID as default value before saving request.
	# id = request.session['id']
	# form = DonationForm(request.POST)
    # form(initial_value{'userID','request.session['id']})
	# Check if valid
	# save to db
	
	if request.method == 'POST':
		
		
		form = DonationForm(request.POST)
		if form.is_valid():
		#obj = form.save(commit = 'false')
		#obj.userID = request.session['id']
		#obj.save();
			form.save();
		return HttpResponse('hi')
	else:
		return render(request, app_name + 'donate_create.html')
		'''
	try:
		form = DonationForm()
		#form(initial={'amount',1})
		form.save()
	except(Exception):
		hi =1
	
	
	return render(request, app_name+'donate_create.html')
	'''
	

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

    
def add_food(request):
    page_data={'myForm':recipeForm(),}
    return render(request, 'audit/Recipes.html',page_data)

def savefood(request):
	if request.method == 'POST':
		form =recipeForm(request.POST)
		if form.is_valid():
			form.save()
		saved_data=FoodForm.objects.all()
		item1=form['nameofItem1']
		item2=form['nameofItem2']
		item3=form['nameofItem3']
		recipe=Recipe.generate_recipe(item1,item2,item3)
		
	return render(request, 'audit/recipefoodsave.html',{'Recipes':recipe})
        