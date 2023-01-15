from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.Signup, name='signup'),
    path('login', views.LoginPage, name='Logingpage'),
    path('logout/', views.logout_view, name='logout'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('formateur_home', views.formateur_home, name='formateur_home'),
    path('zab', views.zab, name='zab'),
    path('etudiant_home', views.etudiant_home, name='etudiant_home')
]

