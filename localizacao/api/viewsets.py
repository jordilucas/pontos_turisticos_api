from rest_framework.viewsets import ModelViewSet
from localizacao.models import Localizacao
from .serializers import EnderecosSerializer

class EnderecosViewSet(ModelViewSet):
    queryset = Localizacao.objects.all()
    serializer_class = EnderecosSerializer