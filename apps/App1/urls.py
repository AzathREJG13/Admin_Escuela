from django.urls import path
from .views import home, register , inicio

urlpatterns = [
    path('registro/', register, name='registro'),
    path('',home, name= 'home'),
    path('inicio/', inicio, name = 'inicio'),

]