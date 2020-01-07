from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import AtracaoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class AtracoesViewSet(ModelViewSet):
   # permission_classes = (IsAuthenticated,)
   # authentication_classes = (TokenAuthentication,)
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer