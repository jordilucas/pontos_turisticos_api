from rest_framework.viewsets import ModelViewSet
from comentarios.models import Comentarios
from .serializers import ComentariosSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class ComentariosViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer