from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('to_do_list/', views.to_do_list, name='to_do_list'),
    path('logout/', views.logout, name='logout')
]