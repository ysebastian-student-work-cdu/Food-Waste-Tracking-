from django.urls import path
from . import views

app_name = 'audit'

urlpatterns = [
    path('create/', views.create_waste_entry, name='create'),
    path('entries/<int:waste_entry_id>/delete/', views.delete_waste_entry, name='delete_entry'),
    path('entries/', views.waste_entries, name='entries'),

    path('items/<int:waste_entry_id>/create/', views.create_waste_item, name='create_item'),
    path('items/<int:waste_item_id>/delete/', views.delete_waste_item, name='delete_item'),
    path('items/<int:waste_entry_id>/', views.waste_items, name='items'),
    
    path('donate', views.donate, name='donate'),
    path('donate/submit', views.submit_donation, name = 'submit_donation'),
    path('donate/past', views.donate_read, name = 'past_donations'),
    path('donate/update', views.donate_update, name = 'update_donations'),
    path('', views.accounts, name='accounts'),
    path('add_food/',views.add_food,name='add_food'),
    path('recipefoodsave.html/',views.savefood,name='savefoodss'),
]