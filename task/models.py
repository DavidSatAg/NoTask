from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tarefa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField(null=True, blank=True)
    completa = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    data_tarefa = models.DateTimeField('data/hora', null=True, blank=True)
    def __str__(self):
        return self.titulo
    class Meta:
        ordering = ['criado_em']
