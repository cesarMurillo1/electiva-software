
from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from .models import *
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
class Inicio(TemplateView):
    template_name='index.html'

def feed(request):
    return render(request, 'index.html')
def register(request):
    msg=None
    if request.method=='POST':
        form=userform(request.POST)
        if form.is_valid():
            user=form.save()
            msg='user create'
            return redirect('login')
        else:
            msg='user no creado'
    else:
        form=userform()
    context={'form':form,'msg':msg}
    return render(request, 'usuario/register.html',context)

def loginview(request):
    form=loginform(request.POST or None)
    msg=None
    if request.method=='POST':
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            usuario=authenticate(username=username,password=password)
            if usuario is not None:
                login(request,usuario)
                return redirect('inicio')
            else:
                msg='credenciales no validas'
        else:
            msg='error de autentificacion'
        
    return render(request, 'usuario/login.html',{'form':form,'msg':msg})
def profile(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    return render(request, 'gestion/profile.html',{'usuario':current_user})
