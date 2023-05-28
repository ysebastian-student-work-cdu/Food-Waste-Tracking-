from django.urls import path
from . import views

app_name = 'audit'

urlpatterns = [
    path('entries/', views.waste_entries, name='entries'),
    path('create/', views.create_waste_entry, name='create'),

    path('waste-items/<int:waste_entry_id>/', views.waste_items_view, name='waste_items'),
    path('donate', views.donate, name='donate'),
    path('submit_donation', views.submit_donation, name = 'submit_donation'),
    path('', views.accounts, name='accounts'),
    path('add_food/',views.add_food,name='add_food'),
    path('recipefoodsave.html/',views.savefood,name='savefoodss'),
    path('waste-items/<int:waste_entry_id>/', views.waste_items_view, name='waste_items'),
]