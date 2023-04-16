from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data_model', views.data_model, name='data_model'),
    path('list', views.list, name='list'),
    path('calculator', views.calculator, name='calculator'),

    path('items/<id>', views.detail),

    # Need to delete below
    
    #path('facts', views.facts, name='facts'),
    #path('reasons', views.reasons, name='reasons'),
    #path('benefits', views.benefits, name='benefits'),
    #path('solutions', views.solutions, name='solutions'),
    #path('resources', views.resources, name='resources'),
    
]
