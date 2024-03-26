
from django.contrib import admin
from django.urls import path
from app_cadastro import views

urlpatterns = [
    #rota, view responsavel, nome de referencia

    path('',views.home,name='home'),
    path('users/', views.users,name='user_list')

]
