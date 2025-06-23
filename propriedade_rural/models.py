from django.db import models

class TipoInsumo(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Tipos de Insumo"

class insumo(models.Model):
    Nome = models.CharField(max_length=45)
    Descricao = models.CharField(max_length=45)
    Tipo = models.ForeignKey(TipoInsumo, on_delete=models.PROTECT)

    def __str__(self):
        return self.Nome

class cultura(models.Model):
    Nome = models.CharField(max_length=50)
    Tempo = models.CharField(max_length=100)

    def __str__(self):
        return self.Nome

class propriedades(models.Model):
    Nome = models.CharField(max_length=50)
    Localizacao = models.CharField(max_length=100)
    Tamanho = models.CharField(max_length=45)

    def __str__(self):
        return f'Nome: {self.Nome} | Localização: {self.Localizacao}'

    class Meta:
        verbose_name_plural = "Propriedades"

class cargo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.ForeignKey(cargo, on_delete=models.PROTECT)
    data_admissao = models.DateField()
    propriedade = models.ForeignKey(propriedades, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


# class plantio(models.Model):
#     areaPlantada = models.CharField(max_length=100000)
#     cultura = models.CharField(max_length=10000)
#     propriedades = models.CharField(max_length=10000)
#     data = models.CharField(max_length=10)

#     def __str__(self):
#         return self.areaPlantada
#         return self.cultura
#         return self.propriedades
#         return self.data


# class uso_insumo(models.Model):
#     quantidade = models.CharField(max_length=1000)
#     dataAplicacao = models.CharField(max_length=10)
#     plantio = models.CharField(max_length=1000)
#     insumo = models.CharField(max_length=8)


#     def __str__(self):
#         return self.quantidade
#         return self.dataAplicacao
#         return self.plantio
#         return self.insumo