from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data_model', views.wastage, name='data_model'),
    path('list', views.list, name='list'),
    path('calculator', views.Calindex, name='calculator'),
    path('analyze', views.calculator, name='calculator_analyzed'),
    path('footer', views.footer, name='footer'),
    path('header', views.header, name='header'),
    # path('solutions', views.solutions, name='solutions'),
    path('impacts', views.impacts, name='impacts'),
    path('items/<id>', views.detail, name='items'),
]
