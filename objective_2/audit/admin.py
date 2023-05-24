from django.contrib import admin
from .models import UserRoles, Users, WasteEntries, WasteItems, Organisation, Donate

# Register your models here.
myModels = [ Organisation, Donate]
admin.site.register(myModels)
