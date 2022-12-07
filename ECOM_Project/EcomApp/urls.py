
from django.urls import path
from EcomApp import views

urlpatterns = [
    path('', views.index, name='index')
]


