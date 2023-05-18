from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('data_model', views.wastage, name='data_model'),
    path('list', views.list, name='list'),
    path('calculator', views.Calindex, name='calculator'),
    path('analyze', views.calculator, name='calculator_analyzed'),
    path('items/<id>', views.detail, name='items'),
    path('<invalid>', views.invalid, name='invalid'),
    path('wastelist', views.wastelist, name='wastelist'),
]
