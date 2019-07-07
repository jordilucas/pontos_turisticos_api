from rest_framework.serializers import ModelSerializer
from localizacao.models import Localizacao

class EnderecosSerializer(ModelSerializer):
    class Meta:
        model = Localizacao
        fields = ('id', 'linha1', 'linha2',
        'cidade', 'estado', 'pais', 'lat', 'lont')