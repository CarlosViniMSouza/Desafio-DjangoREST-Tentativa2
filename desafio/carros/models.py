from django.db import models
from uuid import uuid4

# Create your models here.

class Carros(models.Model):
  id_carro = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  ano = models.IntegerField()
  cor = models.CharField(max_length=15)
  modelo = models.CharField(max_length=10)
  placa = models.CharField(max_length=10)