from django.urls import path
from .views import *

urlpatterns = [
    path('prise/', product_buy),
    path('', product)
]
