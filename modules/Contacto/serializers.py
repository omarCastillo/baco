from rest_framework import serializers
from .models import Contacto, ContactoProductos

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        exclude = ('id',)

class ContactoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactoProductos
        exclude = ('id',)