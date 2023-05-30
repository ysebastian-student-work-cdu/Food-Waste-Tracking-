from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views
#from audit.views import views
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
    path('login/', views.LoginView, name='login'),    
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),     
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),    
    path('welcome/', views.welcome, name='welcome'),
   # path('audit/', views.audit, name='audit'),
    # path('donation/', views.donation, name='donation'),
    path('admin/', admin.site.urls),
]

