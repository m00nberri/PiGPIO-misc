from django.urls import path
from testing import views

urlpatterns = [
    path("", views.home, name='home'),
    path("/GPIO-control", views.GPIOcontrol, name ='GPIOcontrol')
]