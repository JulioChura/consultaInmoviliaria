# models.py
from django.db import models
from cloudinary.models import CloudinaryField
class Propiedad(models.Model):
    TIPO_CHOICES = [
        ('departamento', 'Departamento'),
        ('casa', 'Casa'),
        ('oficina', 'Oficina'),
    ]
    
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    zona = models.CharField(max_length=100)
    descripcion = models.TextField()
    # Upload an image
    imagen = CloudinaryField('image', default="")

    def __str__(self):
        return f"{self.tipo} en {self.zona}"
