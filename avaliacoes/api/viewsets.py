from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avalicaoes
from .serializers import AvaliacoesSerializer

class AvaliacoesViewSet(ModelViewSet):

    queryset = Avalicaoes.objects.all()
    serializer_class = AvaliacoesSerializer