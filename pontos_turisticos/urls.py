from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static 
from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracoesViewSet
from comentarios.api.viewsets import ComentariosViewSet
from localizacao.api.viewsets import EnderecosViewSet
from avaliacoes.api.viewsets import AvaliacoesViewSet

router = routers.DefaultRouter()
router.register(r'pontoturisticos', PontoTuristicoViewSet)
router.register(r'atracoes', AtracoesViewSet)
router.register(r'comentarios', ComentariosViewSet)
router.register(r'enderecos', EnderecosViewSet)
router.register(r'avaliacoes', AvaliacoesViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
