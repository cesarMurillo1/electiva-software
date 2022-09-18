from django.contrib.auth import views
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns=[
    path('',feed,name='index'),
	path('register/', register, name='register'),
<<<<<<< HEAD
	path('login/', loginview, name='login'),
	#path('admin/',admin,name='admin'),
	path('profile/',profile,name='profile')
=======
	path('login/', LoginView.as_view(template_name='gestion/login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='gestion/logout.html'), name='logout'),
    path('profile/',profile,name='profile'),
    path('profileAdmin/',profileAdmin,name='profileAdmin'),
    
>>>>>>> 62aa3cbe7cd2e67765f01aeb56861fb04b378f61
]