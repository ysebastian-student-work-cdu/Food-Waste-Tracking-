from django.urls import path
from . import views

urlpatterns = [
    path('waste-items/<int:waste_entry_id>/', views.waste_items_view, name='waste_items'),
    path('donate', views.donate, name='donate'),
    path('submit_donation', views.submit_donation, name = 'submit_donation'),
    path('', views.accounts, name='accounts'),
path('add_food/',views.add_food,name='add_food'),
    path('recipefoodsave.html/',views.savefood,name='savefoodss')
    path('waste-items/<int:waste_entry_id>/', views.waste_items_view, name='waste_items'),
]