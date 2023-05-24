from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('tables/', views.table_list, name='table_list'),
    path('', admin.site.urls),
]