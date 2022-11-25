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

def inicio2(request):
    return render(request, 'usuario/inicio2.html')

def inicioUsuario(request,username=None):
    Usuarios=usuario.objects.all().exclude(username=username)
    return render(request, 'usuario/inicioUsuario.html',{'username':username,'usuarios':Usuarios})

def UsuariosDisponibles(request,username=None):
    Usuarios=usuario.objects.all().exclude(username=username)
    return render(request, 'usuario/UsuariosDisponibles.html',{'username':username,'usuarios':Usuarios})

def informacion(request,username=None):
    Usuario=usuario.objects.get(username=username)
    return render(request, 'usuario/informacion.html',{'usuario':Usuario})

def enviados(request,username=None,user=None):
    user1 = get_object_or_404(usuario, pk=usuario.objects.get(username=username))
    user2 = get_object_or_404(usuario, pk=usuario.objects.get(username=user))
    form1=docForm(request.POST or None,request.FILES or None)
    form2=enviarForm(request.POST or None)
    if form1.is_valid() and form2.is_valid():
    
        doc = form1.save(commit=False)
        enviado=form2.save(commit=False)
        enviado.destinatario=user1
        enviado.emisario=user2
        doc.save()
        enviado.idDoc=doc
        enviado.save()
        messages.success(request, 'Post enviado')
        return redirect('inicioUsuario',user)

    return render(request, 'usuario/enviados.html',{'archivo':form1,'enviado':form2,'username':username})
def usuariosMensajes(request,username=None):
    user1 = get_object_or_404(usuario, pk=usuario.objects.get(username=username))
    id2=user1.idUsuario
    doc=enviar.objects.filter(
        destinatario=id2,
    )
    return render(request, 'usuario/usuariosMensajes.html',{'doc2':doc,'username':username})

def recibido(request,username=None,user=None):
    emisor = get_object_or_404(usuario, pk=usuario.objects.get(username=username))
    destinatario = get_object_or_404(usuario, pk=usuario.objects.get(username=user))
    id=emisor.idUsuario
    id2=destinatario.idUsuario
    print("ese username: ",username," es te user: ",user)
    doc2=enviar.objects.filter(
        emisario=id,destinatario=id2
    )
    print("es ese",doc2)
    var="idDoc.documento"
    return render(request, 'usuario/recibido.html',{'doc2':doc2,'username':username,'var':var})

def administrador(request,username):
    return render(request, 'usuario/administrador.html',{'username':username})
def loginProfesores1(request):
    form=loginform(request.POST or None)
    msg=None
    if request.method=='POST':
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            usuario=authenticate(username=username,password=password)
            if usuario is not None:
                login(request,usuario)
                return redirect('inicioUsuario',username)
            else:
                msg='credenciales no validas'
        else:
            msg='error de autentificacion'
        
    return render(request, 'usuario/loginProfesores1.html',{'form':form,'msg':msg})

def Registroprofesores(request):
    msg=None
    if request.method=='POST':
        form=userform2(request.POST)
        if form.is_valid():
            form.save()
            msg='user create'
            return redirect('login')
        else:
            msg='user no creado'
    else:
        form=userform2()
    context={'form':form,'msg':msg}
    return render(request, 'usuario/registroprofesores.html',context)

def admin1(request):
    form=loginform(request.POST or None)
    msg=None
    if request.method=='POST':
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            if username=='cesar' and password=='123456':
                return redirect('administrador',username)
            else:
                msg='credenciales no validas'
        else:
            msg='error de autentificacion'
    return render(request, 'usuario/loggin.html',{'form':form,'msg':msg})

def register(request):
    msg=None
    if request.method=='POST':
        form=userform(request.POST)
        if form.is_valid():
            form.save()
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
                return redirect('inicioUsuario',username)
            else:
                msg='credenciales no validas'
        else:
            msg='error de autentificacion'
        
    return render(request, 'usuario/login.html',{'form':form,'msg':msg})

