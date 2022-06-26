from django.contrib import admin
from django.urls import URLPattern, path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('', views.index, name='list'),
    path('update_task/<str:pk>/',views.updatetask, name='update_task'),
    path('delete/<str:pk>/', views.deletetask, name='delete_task'),
]
