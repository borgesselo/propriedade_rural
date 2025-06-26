from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import TipoInsumo
from .serializers import TipoInsumoSerializer

class TipoInsumoViewSet(ModelViewSet):
    queryset = TipoInsumo.objects.all()
    serializer_class = TipoInsumoSerializer

from rest_framework.viewsets import ModelViewSet
from .models import insumo
from .serializers import insumoSerializer

class insumoViewSet(ModelViewSet):
    queryset = insumo.objects.all()
    serializer_class = insumoSerializer

from rest_framework.viewsets import ModelViewSet
from .models import cultura
from .serializers import cultura

class culturaViewSet(ModelViewSet):
    queryset = cultura.objects.all()
    serializer_class = culturaSerializer

from rest_framework.viewsets import ModelViewSet
from .models import propriedades
from .serializers import propriedades

class propriedadesViewSet(ModelViewSet):
    queryset = propriedades.objects.all()
    serializer_class = propriedadesSerializer

from rest_framework.viewsets import ModelViewSet
from .models import cargo
from .serializers import cargo

class cargoViewSet(ModelViewSet):
    queryset = cargo.objects.all()
    serializer_class = cargoSerializer

from rest_framework.viewsets import ModelViewSet
from .models import funcionario
from .serializers import funcionario

class funcionarioViewSet(ModelViewSet):
    queryset = funcionario.objects.all()
    serializer_class = funcionarioSerializer

from rest_framework.viewsets import ModelViewSet
from .models import plantio
from .serializers import plantio

class plantioViewSet(ModelViewSet):
    queryset = plantio.objects.all()
    serializer_class = plantioSerializer

from rest_framework.viewsets import ModelViewSet
from .models import colheita
from .serializers import colheita

class colheitaViewSet(ModelViewSet):
    queryset = colheita.objects.all()
    serializer_class = colheitaSerializer

from rest_framework.viewsets import ModelViewSet
from .models import usoinsumo
from .serializers import usoinsumo

class usoinsumoViewSet(ModelViewSet):
    queryset = usoinsumo.objects.all()
    serializer_class = usoinsumoSerializer
