from django.db import models
from django.contrib.auth.models import User


class Usuario(User):
    tipo = models.CharField('tipo', max_length=200, null = True)
    def __str__(self):
        return '{}'.format(self.username)

class Evento(models.Model):
    administrador = models.ForeignKey(Usuario, null = False)
    nome = models.CharField('nome', max_length=200, null = True)

    def __str__(self):
        return '{}'.format(self.nome)
