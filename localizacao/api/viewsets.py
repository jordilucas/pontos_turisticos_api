from rest_framework.viewsets import ModelViewSet
from localizacao.models import Localizacao
from .serializers import EnderecosSerializer
#from rest_framework.permissions import IsAuthenticated
#from rest_framework.authentication import TokenAuthentication

class EnderecosViewSet(ModelViewSet):
   # permission_classes = (IsAuthenticated,)
   # authentication_classes = (TokenAuthentication,)
    queryset = Localizacao.objects.all()
    serializer_class = EnderecosSerializer