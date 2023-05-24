from django.urls import include, path

urlpatterns = [
    path('admin_console/', include('admin_console.urls')),
    path('', include('users.urls')),
    path('audit/', include('audit.urls')),
    path('accounts/', include('audit.urls')),

]