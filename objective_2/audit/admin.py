'''from django.contrib import admin
from .models import organisation
from .models import Users
from .models import WasteCollection

admin.site.register(organisation)
admin.site.register(Users)
admin.site.register(WasteCollection)

'''

from django.contrib import admin
from .models import Users, UserRoles

# To put tables you want to see in the admin console, add it to the imports above and register it below.

# admin.site.register(myTable)
admin.site.register(Users)
admin.site.register(UserRoles)