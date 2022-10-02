from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu_page, name='menu'),
    path('booking/', views.booking_page, name='booking_page'),
]
