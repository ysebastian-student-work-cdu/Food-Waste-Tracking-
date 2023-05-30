from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timezone
from django.http import HttpResponse
from .forms import CreateWasteEntry
from django.core import serializers
from django.template import loader
from django.urls import reverse
from .models import *
from .forms import *
from .recipe import *
from . import utils



app_name = 'audit/'
sessionid = 1
# Create your views here

def waste_entries(request):
    entries = WasteEntries.objects.all()
    return render(request, 'audit/waste_entries.html', {'entries': entries})

def waste_items(request, waste_entry_id):
    waste_entry = get_object_or_404(WasteEntries, pk=waste_entry_id)
    waste_items = WasteItems.objects.filter(wasteEntryID=waste_entry_id)
    return render(request, 'audit/waste_items.html', {'waste_entry': waste_entry, 'waste_items': waste_items})

def create_waste_entry(request):
    if request.method == 'POST':
        form = CreateWasteEntry(request.POST)
        if form.is_valid():
            form.save()
            return redirect('audit:entries')  # Replace 'blog:posts' with your desired redirect URL
    else:
        form = CreateWasteEntry()
    
    return render(request, 'audit/create_waste_entry.html', {'form': form})

def delete_waste_entry(request, waste_entry_id):
    waste_entry = get_object_or_404(WasteEntries, pk=waste_entry_id)
    waste_entry.delete()
    return redirect('audit:entries')

def create_waste_item(request, waste_entry_id):
    waste_entry = get_object_or_404(WasteEntries, pk=waste_entry_id)

    if request.method == 'POST':
        form = WasteItemForm(request.POST)
        if form.is_valid():
            waste_item = form.save(commit=False)
            waste_item.wasteEntryID = waste_entry
            waste_item.save()
            return redirect('audit:items', waste_entry_id=waste_entry.wasteEntryID)
    else:
        form = WasteItemForm()

    return render(request, 'audit/add_waste_item.html', {'form': form, 'waste_entry': waste_entry})

def delete_waste_item(request, waste_item_id):
    waste_item = get_object_or_404(WasteItems, pk=waste_item_id)
    waste_item.delete()
    return redirect('audit:entries')

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
	request.session['id'] = 3
	form = DonationForm(initial=
        {
            'userID':Users.objects.get(userID = 1),
            'date': datetime.now(timezone.utc)
        }
    )
	page_data = {'myform': form}

	return render(request, app_name + 'donate_create.html', page_data)

def submit_donation(request):
    redir = HttpResponse("valod")
    if request.method == 'POST':
        try:
            model = Donate.objects.get(id=request.POST.get('id'))   # get correct model instance
            form = DonationForm(request.POST, instance = model)
            redir= render(request , app_name+ "donate_update.html")
            form = DonationForm(request.POST)
        except ObjectDoesNotExist:
            form = DonationForm(request.POST)
            redir= render(request , app_name+ "donate_create.html")
        if form.is_valid():
            form.save()
            return HttpResponse("valod")
            
            
    return render(request, app_name +'donate_update.html')
'''
Displays all donations made by user
'''

def donate_read(request):
    forms = []
    dates =[]
    donates = Donate.objects.all().filter(userID = request.session['id'])
    for model in donates:
        forms.append(DonationForm(instance = model))
        
    content = { 'donations': forms}    
    return render(request, app_name + 'donate_read.html', content)

'''
donate_update
'''
def donate_update(request):
    
    forms = []
    ids =[]
    donates = Donate.objects.all().filter(userID=request.session['id'])
    for model in donates:
        forms.append(DonationForm(instance = model))
        ids.append(getattr(model, 'id'))
    content = { 'donations': forms,
                'ids': ids}    
    return render(request, app_name + 'donate_update.html', content)

    

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
        