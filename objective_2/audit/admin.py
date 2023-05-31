from django.contrib import admin
from .models import  WasteEntries, WasteItems, Organisation, Donate,FoodForm,RecipesSaved

# Register your models here.
myModels = [ Organisation, Donate,  FoodForm,RecipesSaved]
admin.site.register(myModels)
