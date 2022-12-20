from django.urls import path
from . import views



urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('', views.home, name='home'),
    path('saveenquiry/', views.saveEnquiry, name='saveenquiry'),

]