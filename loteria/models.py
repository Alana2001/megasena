from django.db import models
from datetime import datetime, date
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class MegaSena(models.Model):
    lista_numeros = models.IntegerField(default=1)
    data_sorteio = models.DateTimeField(default=timezone.now)
    
    def dataaposta(self):
        self.data_sorteio= timezone.now()
        self.save()
    
    def __str__(self):
        return f'lista de numeros: {self.lista_numeros}'

class ApostaClientesMega(models.Model):
    id_cliente = models.CharField(max_length=200, null=False)
    lista_numeros_apostados = models.IntegerField(default=1)
    data_aposta = models.DateTimeField(default=timezone.now)

    def dataaposta(self):
        self.data_aposta= timezone.now()
        self.save()
    
    def __str__(self):
        return self.id_cliente