from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

class usuario(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return F'perfil de {self.user.username}'
