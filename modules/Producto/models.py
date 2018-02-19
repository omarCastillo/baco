from django.db import models
import random
import string

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def image_producto_gral(instance, filename):
	return 'images/{0}/{1}'.format(random_string_generator(),filename)

# Create your models here.
class Linea(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return 'Linea: ' + self.nombre

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    linea = models.ForeignKey(Linea, on_delete=models.CASCADE, related_name='producto')
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return 'Producto: ' + self.nombre

class SubProducto(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='subproducto')
    nombre = models.CharField(max_length=100)
    caracteristica = models.CharField(max_length=300)

    def __str__(self):
        return 'Subproducto: ' + self.nombre + 'Producto: ' + self.producto.nombre

class Presentacion(models.Model):
    id = models.AutoField(primary_key=True)
    presentacion = models.CharField(max_length=100)
    empaque = models.CharField(max_length=100)
    contenido = models.CharField(max_length=100)

    def __str__(self):
        return 'Empaque: ' + self.empaque + ' Contenido: ' + self.contenido

class Color(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    clave = models.CharField(max_length=10)

    def __str__(self):
        return 'Color: ' + self.nombre + ' Clave: ' + self.clave

class DetalleProducto(models.Model):
    id = models.AutoField(primary_key=True)
    subproducto = models.ForeignKey('SubProducto', on_delete=models.CASCADE, related_name='detalle')
    nombre = models.CharField(max_length=100)
    especificaciones = models.CharField(max_length=300)
    clave = models.CharField(max_length=20)
    medidas = models.CharField(max_length=40)
    peso = models.DecimalField(max_digits=10,decimal_places=2)
    presentaciones = models.ManyToManyField(Presentacion, blank=True)
    colores = models.ManyToManyField(Color, blank=True)
    imagen = models.ImageField(upload_to=image_producto_gral, blank=True, null=True)

    def __str__(self):
        return 'Detalle de: ' + self.subproducto.nombre + ' Clave: ' + self.clave
