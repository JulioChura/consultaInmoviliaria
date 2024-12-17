from django.db import models

# Modelo para la tabla viviendas
from django.db import models

class Vivienda(models.Model):
    tipo_choices = [
        ('Piso', 'Piso'),
        ('Casa', 'Casa'),
        ('Chalet', 'Chalet'),
    ]
    tipo = models.CharField(max_length=50, choices=tipo_choices)
    zona = models.CharField(max_length=255)
    ndormitorios = models.IntegerField()
    metros_cuadrados = models.DecimalField(max_digits=6, decimal_places=2)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    garaje = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.tipo} en {self.zona}'

class LnDiccionario(models.Model):
    palabra = models.CharField(max_length=255)

    def __str__(self):
        return self.palabra

class LnPatron(models.Model):
    patron = models.CharField(max_length=255)
    consulta_sql = models.TextField()

    def __str__(self):
        return self.patron

