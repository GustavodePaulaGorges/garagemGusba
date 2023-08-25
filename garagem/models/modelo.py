from django.db import models

from .categoria import Categoria
from .marca import Marca


class Modelo(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="modelos")
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name="modelos")
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome.upper()