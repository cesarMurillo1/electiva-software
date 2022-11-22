from time import time
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User,AbstractUser
# Create your models here.

class usuario(AbstractUser): 
    idUsuario = models.CharField(primary_key=True,max_length=11)
    codigoRegistro = models.CharField(max_length=11)
    nombre = models.CharField(max_length=11)
    programa = models.CharField(max_length=100, null=False)
    programa2 = models.CharField(max_length=100)
    def __str__(self):
        return F'{self.idUsuario}'
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
#MODEL DEL DOCUMENTO
class documento(models.Model): 
    idDoc = models.AutoField(primary_key=True)
    documento=models.FileField(upload_to="archivo/",blank=True,null=True)
    class Meta:
        verbose_name = 'documento'
        verbose_name_plural = 'documentos'

#MODEL DE ENVIO DE DOCUMENTO/DOCUMENTOS
class enviar(models.Model): 
    idEnvio = models.AutoField(primary_key=True,  null=False)
    idDoc = models.ForeignKey(documento,on_delete=models.CASCADE,related_name='docs1')
    destinatario = models.ForeignKey(usuario,on_delete=models.CASCADE,related_name='docs1')
    emisario = models.ForeignKey(usuario,on_delete=models.CASCADE,related_name='docs2')
    fecha = models.DateTimeField(auto_now=True, auto_now_add=False)
    mensaje = models.TextField(max_length=1000)
    etiqueta = models.CharField(max_length=50, null=False)
    class Meta:
        verbose_name = 'enviar'
        verbose_name_plural = 'enviados'

#MODEL DE LA COLECCIÓN DE DOCUMENTOS
class coleccion(models.Model): 
    idColec = models.CharField(primary_key=True, max_length=30, null=False)
    idEnvio = models.ForeignKey(enviar,on_delete=models.CASCADE,related_name='enviar')
    
#MODEL DEL REPORTE QUE EL ADMINISTRADOR DEBE REALIZAR
#class reporte(models.Model): 
#    idReporte = models.CharField(primary_key=True, max_length=30, null=False)
#    idColec = models.CharField(max_length=30, null=False)
#    idEnvio = models.CharField(max_length=30, null=False)
#    descripcion = models.TextField(max_length=1000, null=False)  