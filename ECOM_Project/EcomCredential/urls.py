from django.urls import path
from EcomCredential import views

app_name = 'EcomCredential'
urlpatterns = [
    path('register/', views.Register, name='register')
]
