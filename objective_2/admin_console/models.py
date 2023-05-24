from django.contrib import admin
from audit.models import Users, UserRoles, WasteEntries, WasteItems

class admin_Users(admin.ModelAdmin):
    ordering = ('userID',)

class admin_UserRoles(admin.ModelAdmin):
    ordering = ('roleID',)

class admin_WasteEntries(admin.ModelAdmin):
    ordering = ('wasteEntryID',)

class admin_WasteItems(admin.ModelAdmin):
    ordering = ('wasteItemID',)

admin.site.register(Users, admin_Users)
admin.site.register(UserRoles, admin_UserRoles)
admin.site.register(WasteEntries, admin_WasteEntries)
admin.site.register(WasteItems, admin_WasteItems)