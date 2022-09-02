from django.contrib.auth import views
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns=[
    path('',feed,name='index'),
	path('register/', register, name='register'),
	path('login/', LoginView.as_view(template_name='gestion/login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='gestion/logout.html'), name='logout'),
    path('profile/',profile,name='profile'),
    path('profileAdmin/',profileAdmin,name='profileAdmin'),
    
]