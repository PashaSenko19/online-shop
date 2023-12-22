from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('chekout/', views.chekout, name='checkout'),

    path('update_item/', views.updateItem, name='updateItem'),
    path('process_order/', views.processOrder, name='processOrder'),
]
