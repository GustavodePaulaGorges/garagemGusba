from django.contrib import admin

from .models import Marca, Categoria, Acessório, Cor, Veículo


admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Acessório)
admin.site.register(Cor)
admin.site.register(Veículo)
