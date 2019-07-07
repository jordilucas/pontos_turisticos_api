from rest_framework.serializers import ModelSerializer
from avaliacoes.models import Avalicaoes

class AvaliacoesSerializer(ModelSerializer):
    class Meta:
        model = Avalicaoes
        fields = ('id', 'user', 'comentario', 
        'nota', 'data')