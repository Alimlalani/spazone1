from django.urls import path
from . import views

urlpatterns = [
    # add URL patterns for your app here
    path('home',views.home, name ='home'),

]
