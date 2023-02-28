"""Appoint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin


from django.urls import path
from . import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.home, name='home'),
    path('payment',views.payment , name='payment'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('login_view/', views.login_view , name='login_view'),
    path('logout/', views.logout, name='logout'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('payment/', views.process_payment, name='process_payment'),
    path('appointments/', views.manage_appointment, name='manage_appointments'),
    path('view_appointments/', views.view_appointments, name='view_appointments'),

]

