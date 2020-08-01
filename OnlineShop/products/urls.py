from django.urls import path
from . import views

urlpatterns = [
    path('', views.Products_Index.as_view(), name='products_index'),
    path('new/', views.Products_New.as_view(), name='products_new'),

]
