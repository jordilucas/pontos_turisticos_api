from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentarios
from avaliacoes.models import Avalicaoes
from localizacao.models import Localizacao

class PontoTuristico(models.Model):
    nome =  models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField()
    atracao = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentarios)
    avaliacoes = models.ManyToManyField(Avalicaoes)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

