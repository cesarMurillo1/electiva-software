import email
from socket import fromshare
from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from app.models import usuario,documento,enviar



class docForm(forms.ModelForm):
    class Meta:
        model=documento
        fields=['documento']

class enviarForm(forms.ModelForm):
    class Meta:
        model=enviar
        fields=['mensaje','etiqueta']

class userform(UserCreationForm):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    
    password1=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password2=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    email=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )    
    class Meta:
        model=usuario
        fields=('username','email','password1','password2','idUsuario','codigoRegistro','programa','programa2')
        help_text={k:""for k in fields}

class loginform(forms.Form):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control"
            }
        )
    )
    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class":"form-control"
            }
        )
    )