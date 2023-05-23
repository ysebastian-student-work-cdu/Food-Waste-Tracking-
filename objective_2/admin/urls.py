from django.contrib import admin
from django.urls import path
from . import views

from .views import table_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tables/', table_list, name='table_list'),
]
