from django.db.models.query import QuerySet
from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from .models import *
from django.contrib import messages
from django.views.generic import TemplateView,ListView,UpdateView
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login
from django.core.files.storage import FileSystemStorage

def inicio(request):
    return render(request, 'inicio.html')

def inicioUsuario(request,username=None):
    return render(request, 'usuario/inicioUsuario.html',{'username':username})

def admin(request):
    return render(request, 'admin.html')
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
                p="inicioUsuario/"+username
                return redirect(p)
            else:
                msg='credenciales no validas'
        else:
            msg='error de autentificacion'
        
    return render(request, 'usuario/login.html',{'form':form,'msg':msg})

def documentos(request,username=None):
    current_user=usuario.objects.get(username=username)
    form1=docForm(request.POST or None,request.FILES or None)
    if form1.is_valid():
        doc = form1.save(commit=False)
        doc.usuario = current_user
        doc.save()
        messages.success(request, 'Post enviado')
        return redirect('inicioUsuario')
    return render(request,'usuario/crearDoc.html',{'form':form1})