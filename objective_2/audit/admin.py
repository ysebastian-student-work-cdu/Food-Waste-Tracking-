from django.contrib import admin
from .models import UserRoles, Users, WasteEntries, WasteItems, Organisation, Donate,FoodForm,Payment

# Register your models here.
myModels = [ Organisation, Donate,  FoodForm, Payment ]
admin.site.register(myModels)
