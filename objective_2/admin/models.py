from django.contrib import admin
from audit.models import Users, UserRoles


admin.site.register(Users)
admin.site.register(UserRoles)
