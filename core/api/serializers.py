from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer 
from comentarios.api.serializers import ComentariosSerializer
from avaliacoes.api.serializers import AvaliacoesSerializer
from localizacao.api.serializers import EnderecosSerializer

class PontoTuristicoSerializer(ModelSerializer):
    atracao = AtracaoSerializer(many=True)
    comentarios = ComentariosSerializer(many=True)
    avaliacoes = AvaliacoesSerializer(many=True)
    localizacao = EnderecosSerializer()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao','foto','aprovado',
                  'atracao','comentarios','avaliacoes','localizacao')