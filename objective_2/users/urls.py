from django.urls import path, include
from . import views
from audit.views import views
# from accounts import views


urlpatterns = [
    path('', views.index, name='index'),
    path('data_model', views.wastage, name='data_model'),
    path('list', views.list, name='list'),
    path('calculator', views.Calindex, name='calculator'),
    path('analyze', views.calculator, name='calculator_analyzed'),
    path('items/<id>', views.detail, name='items'),
    path('<invalid>', views.invalid, name='invalid'),
    path('wastelist', views.wastelist, name='wastelist'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('signup/', views.Signup, name='signup'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('welcome/', views.welcome, name='welcome'),
    path('audit/', views.audit, name='audit'),
]

