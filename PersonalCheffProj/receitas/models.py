from django.db import models
from datetime import datetime

class Receitas(models.Model):
    nome_receitas = models.CharField(max_length=180)
    video = models.CharField(max_length=88)
    modo_preparo = models.TextField()
    ingredientes = models.TextField()
    nota = models.IntegerField()
    data_receita = models.DateTimeField(default=datetime.now, blank=True)

# Create your models here.
