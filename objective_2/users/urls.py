from django.urls import path, include
from django.contrib import admin
#from django.contrib.auth import views as auth_views

from . import views
#from audit.views import views
# from accounts import views


urlpatterns = [

    path('', views.index, name='index'),
    path('data_model', views.wastage, name='data_model'),
    path('calculator', views.Calindex, name='calculator'),
    path('analyze', views.calculator, name='calculator_analyzed'),
    path('items/<id>', views.detail, name='items'),
    path('<invalid>', views.invalid, name='invalid'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('signup/', views.Signup, name='signup'),
    path('login/', views.LoginView, name='login'), 
    path('logout/', views.LogoutView, name='logout'), 
    #path('audit/', views.audit, name='audit'),
    path('admin/', admin.site.urls),
]

