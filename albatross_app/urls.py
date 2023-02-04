from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('homepage/', views.homepage, name='homepage'),
    path('user_login/', views.user_login, name="user_login"),
    path('user_profile/', views.user_profile, name="user_profile"),
    path('technology/', views.technology, name="technology"),
    path('about/', views.about, name="about"),
    path('merch_tent/', views.merch_tent, name="merch_tent"),
    path('admin/', admin.site.urls),
]