from django.contrib.auth import views as auth_views
from django.urls import path
from .payment import *
from . import views

app_name = 'audit'

urlpatterns = [
    path('', views.auditHome, name='auditHome'),

    path('login/', views.LoginView, name='login'),    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),    
    

    path('create/', views.create_waste_entry, name='create'),
    path('entries/<int:waste_entry_id>/delete/', views.delete_waste_entry, name='delete_entry'),
    path('entries/', views.waste_entries, name='entries'),

    path('items/<int:waste_entry_id>/create/', views.create_waste_item, name='create_item'),
    path('items/<int:waste_item_id>/delete/', views.delete_waste_item, name='delete_item'),
    path('items/<int:waste_entry_id>/', views.waste_items, name='items'),
    
    path('donate', views.donate, name='donate'),
   path('donate/past', views.donate_read, name = 'past_donations'),
    path('donate/update', views.donate_update, name = 'update_donations'),
    path('', views.accounts, name='accounts'),
    path('add_food/',views.add_food,name='add_food'),
    path('recipefoodsave.html/',views.savefood,name='savefoodss'),
   # path('initiate-payment/', views.initiate_payment, name='initiate_payment'),
   # path('complete-payment/<int:payment_id>/', views.complete_payment, name='complete_payment'),
]