from rest_framework.serializers import ModelSerializer
from .models import TipoInsumo

class TipoInsumoSerializer(ModelSerializer):
    class Meta:
        model = TipoInsumo
        fields = '__all__'

from rest_framework.serializers import ModelSerializer
from .models import insumo

class insumoSerializer(ModelSerializer):
    class Meta:
        model = insumo
        fields = '__all__'

from rest_framework.serializers import ModelSerializer
from .models import cultura

class culturaSerializer(ModelSerializer):
    class Meta:
        model = cultura
        fields = '__all__'

from rest_framework.serializers import ModelSerializer
from .models import propriedades

class propriedadesSerializer(ModelSerializer):
    class Meta:
        model = propriedades
        fields = '__all__'

from rest_framework.serializers import ModelSerializer
from .models import cargo

class cargoSerializer(ModelSerializer):
    class Meta:
        model = cargo
        fields = '__all__'

from rest_framework.serializers import ModelSerializer
from .models import funcionario

class funcionarioSerializer(ModelSerializer):
    class Meta:
        model = funcionario
        fields = '__all__'

from rest_framework.serializers import ModelSerializer
from .models import plantio

class plantioSerializer(ModelSerializer):
    class Meta:
        model = plantio
        fields = '__all__'

from rest_framework.serializers import ModelSerializer
from .models import colheita

class colheitaSerializer(ModelSerializer):
    class Meta:
        model = colheita
        fields = '__all__'

from rest_framework.serializers import ModelSerializer
from .models import usoinsumo

class usoinsumoSerializer(ModelSerializer):
    class Meta:
        model = usoinsumo
        fields = '__all__'