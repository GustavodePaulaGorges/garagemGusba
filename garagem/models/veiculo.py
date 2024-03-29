from django.db import models

from uploader.models import Image
from .acessorio import Acessorio
from .cor import Cor
from .modelo import Modelo



class Veiculo(models.Model):
    cor = models.ForeignKey(Cor, on_delete=models.CASCADE)
    ano = models.IntegerField(null=True, blank=True, default=0)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, related_name="veiculos")
    descricao = models.CharField(
        max_length=300, null=True, blank=True, default="Sem descrição"
    )
    preco = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0
    )
    acessorios = models.ManyToManyField(Acessorio, blank=True, related_name="veiculos")
    imagem = models.ManyToManyField(Image, related_name="+", blank=True)

    def __str__(self):
        return f"{self.modelo} | {self.cor} | {self.ano}"

    class Meta:
        verbose_name = "Veículo"

    class Meta:
        verbose_name_plural = "Veículos"
