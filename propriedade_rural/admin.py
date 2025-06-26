from django.contrib import admin
from .models import TipoInsumo, insumo, propriedades, funcionario, cargo, plantio, colheita, usoinsumo

admin.site.register(TipoInsumo)
admin.site.register(insumo)
admin.site.register(propriedades)
admin.site.register(funcionario)
admin.site.register(cargo)
admin.site.register(plantio)
admin.site.register(colheita)
admin.site.register(usoinsumo)
