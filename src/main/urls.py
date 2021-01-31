from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.About.as_view(), name='about-us'),
    path('weather', views.weather, name='weather'),
    path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('task/', views.TaskView.as_view()),
    path('search/', views.Search.as_view(), name='search'),
]
