from django.db import models
from django.utils import timezone

# class Localidad(models.Model):
#     nombre = models.CharField(max_length=100)
#     coordenadas = models.CharField(max_length=100)
#     cod_postal = models.CharField(max_length=5)

#     def __str__(self):
#         return self.nombre

# class Agente(models.Model):
#     nombre = models.CharField(max_length=100)
#     email = models.EmailField()
#     telefono = models.CharField(max_length=9, blank=True, null=True)
#     direccion = models.CharField(max_length=100, blank=True, null=True)
#     tipo_de_agente = models.CharField(max_length=100)
#     localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.nombre

# class Departamento(models.Model):
#     nombre = models.CharField(max_length=100)
#     localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
#     agente = models.ForeignKey(Agente, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.nombre

# class Foto(models.Model):
#     departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
#     imagen = models.ImageField(upload_to='fotos/')
#     descripcion = models.CharField(max_length=100)

#     def __str__(self):
#         return f"Foto de {self.departamento.nombre}"

# class Usuario(models.Model):
#     nombre = models.CharField(max_length=100)
#     contraseña = models.CharField(max_length=100)
#     email = models.EmailField()
#     telefono = models.CharField(max_length=9, blank=True, null=True)
#     direccion = models.CharField(max_length=100, blank=True, null=True)
#     localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.nombre

# class Favorito(models.Model):
#     usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
#     departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.usuario.nombre} ha marcado como favorito {self.departamento.nombre}"
    
class Listing(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    property_type = models.CharField(max_length=20, choices=(('apartment', 'Apartment'), ('house', 'House')))
    num_bedrooms = models.IntegerField()
    price_min = models.DecimalField(max_digits=10, decimal_places=2)
    price_max = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(default=timezone.now) 

    def __str__(self):
        return self.name
