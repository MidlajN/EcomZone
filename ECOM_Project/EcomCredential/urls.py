from django.urls import path
from EcomCredential import views

app_name = 'EcomCredential'
urlpatterns = [
    path('register/', views.Register, name='register'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout')
]
