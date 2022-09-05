from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

   
#MODEL DEL REGISTRO DE USUARIO (ADMINISTRADOR Y ESTUDIANTE)
class usuario(models.Model): 
    codigoRegistro = models.CharField(primary_key=True, max_length=11, null=False)
    nombre = models.CharField(max_length=100, null=False)
    contrasena = models.CharField(max_length=15, null=False)
    correoUsu = models.CharField(max_length=50, null=False)
    programa = models.CharField(max_length=100, null=False)
    programa2 = models.CharField(max_length=100)
    rol = models.CharField(max_length=50, null=False)
    def __str__(self):
        return F'perfil de {self.codigoRegistro}'

#MODEL DEL DOCUMENTO
class documento(models.Model): 
    idDoc = models.CharField(primary_key=True, max_length=30, null=False)
    tipoDocumento = models.CharField(max_length=50, null=False)
    rutaDoc = models.CharField(max_length=200, null=False)
    
#MODEL DE ENVIO DE DOCUMENTO/DOCUMENTOS
class enviar(models.Model): 
    idEnvio = models.CharField(primary_key=True, max_length=30, null=False)
    codigoRegistro = models.CharField(max_length=11, null=False)
    idDoc = models.CharField(max_length=30, null=False)
    destinatario = models.CharField(max_length=100, null=False)
    emisario = models.CharField(max_length=100, null=False)
    fecha = models.DateTimeField(default=timezone.now, null=False)
    mensaje = models.CharField(max_length=200)
    etiqueta = models.CharField(max_length=200, null=False)
    
#MODEL DE LA COLECCIÓN DE DOCUMENTOS
class coleccion(models.Model): 
    idColec = models.CharField(primary_key=True, max_length=30, null=False)
    idEnvio = models.CharField(max_length=30, null=False)
    
#MODEL DEL REPORTE QUE EL ADMINISTRADOR DEBE REALIZAR
class reporte(models.Model): 
    idReporte = models.CharField(primary_key=True, max_length=30, null=False)
    idColec = models.CharField(max_length=30, null=False)
    idEnvio = models.CharField(max_length=30, null=False)
    descripcion = models.TextField(max_length=10000, null=False)  
    
#RECUERDEN CAMBIAR LA CONTRASEÑA DEL POSTGRES POR LA SUYA