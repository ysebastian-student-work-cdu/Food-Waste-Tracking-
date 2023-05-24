from django.contrib import admin
from django.urls import path

from .views import table_list

urlpatterns = [
    path('', admin.site.urls),
    path('tables/', table_list, name='table_list'),
]