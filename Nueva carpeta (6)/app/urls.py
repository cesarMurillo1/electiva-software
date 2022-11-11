from django.contrib.auth import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView
from .views import *

urlpatterns=[
    path('',inicio,name='inicio'),
	path('register/', register, name='register'),
	path('login/', loginview, name='login'),
	path('admin/',admin,name='admin'),
	path('login/inicioUsuario/<str:username>/', inicioUsuario, name='inicioUsuario'),
	path('crearDoc/<str:username>/', documentos, name='crearDoc'),
]

