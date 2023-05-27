from django.urls import path
from . import views

urlpatterns = [
    path('waste-items/<int:waste_entry_id>/', views.waste_items_view, name='waste_items'),
    path('donate', views.donate, name='donate'),
    path('submit_donation', views.submit_donation, name = 'submit_donation'),
    path('', views.accounts, name='accounts'),
]