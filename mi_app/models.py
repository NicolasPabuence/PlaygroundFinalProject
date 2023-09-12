from django.db import models

class CategoriaZapatos(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Zapato(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(CategoriaZapatos, on_delete=models.CASCADE)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class ComentarioZapato(models.Model):
    zapato = models.ForeignKey(Zapato, on_delete=models.CASCADE)
    texto = models.TextField()

    def __str__(self):
        return self.texto
