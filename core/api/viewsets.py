from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class PontoTuristicoViewSet(ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer