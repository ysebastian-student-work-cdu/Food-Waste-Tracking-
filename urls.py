from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.list, name='list'),
    path('detail', views.detail, name='detail'),
    path('data_model', views.data_model, name='data_model'),
]
