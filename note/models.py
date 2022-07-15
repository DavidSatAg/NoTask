from django.db import models

# Create your models here.

class Anotacao(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('criado_em')

    def __str__(self):
        return self.titulo