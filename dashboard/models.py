from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORIA=(
    ('Papeleria','Papeleria'),
    ('Electronica','Electronica'),
    ('Comida','Comida'),
)

class Producto(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIA,null=True)
    cantidad = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.nombre}-{self.cantidad}'
    
class Orden(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)
    personal = models.ForeignKey(User, models.CASCADE,null=True)
    cantidad_de_orden = models.PositiveIntegerField(null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural ='Ordenes'

    def __str__(self):
        return f'{self.producto} ordenado por {self.personal.username}'