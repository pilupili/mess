from django.contrib import admin
from django.urls import path,include
from signin import views

urlpatterns = [
    path('',views.login,name='login'),path('register/', views.register, name='register'),path('signin/', views.signin, name='signin'),
    path('home/', views.sidebar, name='sidebar'),path('home/logout/',views.logout,name='logout'),
    path('home/profile/',views.profile,name='profile'),path('home/profile/update/',views.update,name='update')
    
]