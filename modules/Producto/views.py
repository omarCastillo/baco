from .models import Linea, Producto, DetalleProducto
from .serializers import LineaSerializer, ProductoSerializer, DetalleProductoSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class LineaView(generics.ListAPIView):
    queryset = Linea.objects.all()
    serializer_class = LineaSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = {
        'nombre': ['contains']
    }

class ProductoView(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id',)

class DetalleView(generics.ListAPIView):
    queryset =  DetalleProducto.objects.all()
    serializer_class = DetalleProductoSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id','clave')