
from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from .models import *
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.models import User

class Inicio(TemplateView):
    template_name='index.html'

def feed(request):
    return render(request, 'index.html')

def register(request):
    if request.method=='POST':
        form=userRegisterform(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request,f'Usuario{username} creado')
            return redirect('index')
    else:
        form=userRegisterform()
    context={'form':form}
    return render(request, 'gestion/register.html',context)

def profile(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    return render(request, 'gestion/profile.html',{'usuario':current_user})

def profileAdmin(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    return render(request, 'gestion/profileAdmin.html',{'usuario':current_user})