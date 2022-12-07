
from django.urls import path
from EcomApp import views

app_name = 'EcomApp'
urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat, name='product_by_category')
]


