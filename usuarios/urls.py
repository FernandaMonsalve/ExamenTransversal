#from django.conf.urls import url
from django.urls import path
from  . import views



urlpatterns = [
   path('index', views.index, name='index'),

   path('crud',views.crud,name='crud'),
   path('usuariosAdd',views.usuariosAdd,name='usuariosAdd'),
   path('usuarios_del/<str:pk>', views.usuarios_del, name='usuarios_del'),
   path('usuarios_findEdit/<str:pk>', views.usuarios_findEdit, name='usuarios_findEdit'),
   path('usuariosUpdate', views.usuariosUpdate, name='usuariosUpdate'),
] 
