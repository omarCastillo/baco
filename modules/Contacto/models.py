from django.db import models
from modules.Producto.models import DetalleProducto
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


def EnviarContacto(asunto,email,mensaje,nombre,mail_envio):
    html = get_template('mail/baco-mensaje.html')
    html2 = get_template('mail/baco-mensaje-respuesta.html')
    data = {
        'asunto':asunto,
        'email':email,
        'mensaje':mensaje,
        'nombre':nombre,
        'mail_envio':mail_envio
    }
    html_content = html.render(data)
    html2 = html2.render()
    message = EmailMultiAlternatives(asunto, 'Mensaje de Baco', email, [mail_envio])
    message2 = EmailMultiAlternatives('Gracias por ponerte en contacto con nosotros', 'Mensaje de Baco', mail_envio, [email])
    message.attach_alternative(html_content, 'text/html')
    message2.attach_alternative(html2, 'text/html')
    message.send()
    message2.send()

def EnviarProducto(asunto,email,pedido,nombre,mail_envio,id,request):
    html = get_template('mail/baco-pedido.html')
    html2 = get_template('mail/baco-pedido-respuesta.html')
    data = {
        'asunto':asunto,
        'email':email,
        'pedido':pedido,
        'nombre':nombre,
        'mail_envio':mail_envio,
        'id':id,
        'telefono':request['telefono'],
        'direccion':request['direccion'],
        'cliente':request['cliente']
    }
    html_content = html.render(data)
    html2 = html2.render(data)
    message = EmailMultiAlternatives(
        'Mensaje enviado desde pedidos ' + asunto, 'Mensaje de Baco', email, [mail_envio]
        )
    message2 = EmailMultiAlternatives(
        'Gracias por ponerte en contacto con nosotros', 'Mensaje de Baco', mail_envio, [email]
        )
    message.attach_alternative(html_content, 'text/html')
    message2.attach_alternative(html2, 'text/html')
    message.send()
    message2.send()

# Create your models here.
class Contacto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    asunto = models.CharField(max_length=60)
    mensaje = models.TextField()
    mail_envio = models.EmailField()

    def __str__(self):
        return self.nombre + ' ' + self.email + ' ' + self.asunto


class ContactoProductos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    asunto = models.CharField(max_length=60)
    pedido = models.TextField()
    mail_envio = models.EmailField()
    cliente = models.BigIntegerField(blank=True, null=True)
    telefono = models.BigIntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre + ' ' + self.email + ' ' + self.asunto
