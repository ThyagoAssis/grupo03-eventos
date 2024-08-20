from django.db import models
import datetime

# Create your models here.
class Evento(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    data = models.DateField(default='DD-MM-YYYY',null=True, blank=True)
    hora = models.TimeField(default=datetime.time(9, 0),null=True, blank=True)
    numero_convidados = models.CharField(max_length=30,null=False, blank=False)
    local = models.CharField(max_length=100,null=False, blank=False)