from django.contrib.auth import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView
from .views import *
urlpatterns=[
    path('',inicio,name='inicio'),
	path('inicio2/',inicio2,name='inicio2'),
	path('register/', register, name='register'),
	path('registroprofesores/', Registroprofesores, name='registroprofesores'),
	path('login/', loginview, name='login'),
	path('loginProfesores1/', loginProfesores1, name='loginProfesores1'),
	path('loggin/',admin1,name='loggin'),
	path('login/inicioUsuario/<str:username>/', inicioUsuario, name='inicioUsuario'),
	path('enviados/<str:user>/<str:username>/', enviados, name='enviados'),
	path('recibido/<str:user>/<str:username>/', recibido, name='recibido'),
	path('UsuariosDisponibles/<str:username>/', UsuariosDisponibles, name='UsuariosDisponibles'),
	path('informacion/<str:username>/', informacion, name='informacion'),
	path('administrador/<str:username>/', administrador, name='administrador'),
	path('logout/', LogoutView.as_view(template_name='usuario/logout.html'), name='logout'),
	path('usuariosMensajes/<str:username>/', usuariosMensajes, name='usuariosMensajes'),
	
]