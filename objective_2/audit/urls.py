from django.urls import path
from . import views

urlpatterns = [
    path('donate', views.donate_create),
    path('accounts/', views.index, name='index'),
]