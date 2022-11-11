from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser


class usuario(AbstractUser): 
    idUsuario = models.CharField(primary_key=True,max_length=11)
    codigoRegistro = models.CharField(max_length=11)
    nombre = models.CharField(max_length=11)
    programa = models.CharField(max_length=100, null=False)
    programa2 = models.CharField(max_length=100)
    def __str__(self):
        return F'perfil de {self.nombre}'

