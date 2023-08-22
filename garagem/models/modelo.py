from django.db import models

from .categoria import Categoria
from .marca import Marca


class Modelo(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
