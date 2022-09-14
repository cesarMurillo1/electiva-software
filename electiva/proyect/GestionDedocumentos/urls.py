from django.contrib.auth import views
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns=[
    path('',feed,name='index'),
	path('register/', register, name='register'),
	path('login/', loginview, name='login'),
	#path('admin/',admin,name='admin'),
	path('profile/',profile,name='profile')
]