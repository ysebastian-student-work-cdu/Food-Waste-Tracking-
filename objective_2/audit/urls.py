from django.urls import path
from . import views

urlpatterns = [
    path('', views.accounts, name='accounts'),
    path('waste-items/<int:waste_entry_id>/', views.waste_items_view, name='waste_items'),
    path('add_food/',views.add_food,name='add_food'),
    path('recipefoodsave.html/',views.savefood,name='savefoodss')
]