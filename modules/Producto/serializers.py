from rest_framework import serializers
from .models import Linea, Producto, SubProducto, DetalleProducto, Presentacion, Color

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class PresentacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentacion
        fields = ('empaque', 'contenido')

class DetalleProductoSerializer(serializers.ModelSerializer):
    presentaciones = PresentacionSerializer(many=True)
    colores = ColorSerializer(many=True)
    class Meta:
        model = DetalleProducto
        fields = '__all__'

class SubProductoSerialiser(serializers.ModelSerializer):
    detalle = DetalleProductoSerializer(many=True)
    class Meta:
        model = SubProducto
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    subproducto = SubProductoSerialiser(many=True)
    class Meta:
        model = Producto
        fields = ('nombre','subproducto','id')

class LineaSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(many=True)
    class Meta:
        model = Linea
        fields = ('nombre','producto')