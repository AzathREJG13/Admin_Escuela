from django.urls import path
from .views import home, register 

urlpatterns = [
    path('registro/', register, name='registro'),
    path('',home, name= 'home'),

]