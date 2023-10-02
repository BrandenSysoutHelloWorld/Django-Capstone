# Imports
from django.contrib import admin
from django.urls import path, include

# Resolve URL Route's(Application's Map)
urlpatterns = [
    path('admin/', admin.site.urls), # Admin Dashboard
    path('users/', include('users.urls')), # Users Application
    path('', include('eskak.urls')), # Eskak Application(ROOT PATH)
    
]

'''CODE IMPLEMENTED & CONTRIBUTED BY: BRANDEN VAN STADEN'''
