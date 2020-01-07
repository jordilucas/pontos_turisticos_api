from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avalicaoes
from .serializers import AvaliacoesSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class AvaliacoesViewSet(ModelViewSet):
   # permission_classes = (IsAuthenticated,)
   # authentication_classes = (TokenAuthentication,)
    queryset = Avalicaoes.objects.all()
    serializer_class = AvaliacoesSerializer