from django.urls import path
from testing import views

urlpatterns = [
    path("", views.home, name='home'),
    path("testing/<name>", views.testlink, name='testlink68')
]