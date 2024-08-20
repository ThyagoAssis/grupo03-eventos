from django.db import models

# Create your models here.
class Evento(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    data2 = models.DateField(null=False)
    numero_convidados = models.CharField(max_length=30,null=False, blank=False)
    local = models.CharField(max_length=100,null=False, blank=False)