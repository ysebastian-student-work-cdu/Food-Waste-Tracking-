from django.contrib import admin
from .models import  WasteEntries, WasteItems, Organisation, Donate,FoodForm

# Register your models here.
myModels = [ Organisation, Donate,  FoodForm]
admin.site.register(myModels)
