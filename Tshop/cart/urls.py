from django.urls import path 

from . import views

urlpatterns = [
    path('', views.CartView.as_view(), name = 'view_cart')   
    # path('', views.view_cart, name = 'view_cart')
]