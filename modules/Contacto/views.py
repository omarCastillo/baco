from .models import Contacto, ContactoProductos, EnviarContacto, EnviarProducto
from .serializers import ContactoSerializer, ContactoProductoSerializer
from rest_framework import generics, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

# Create your views here.
class ContactoView(generics.CreateAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer

    def create(self, request):
        serializer = ContactoSerializer(data=request.data)
        if serializer.is_valid():
            EnviarContacto(request.data['asunto'], request.data['email'], request.data['mensaje'], request.data['nombre'], request.data['mail_envio'])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class ContactoProductoView(generics.CreateAPIView):
    queryset = ContactoProductos.objects.all()
    serializer_class = ContactoProductoSerializer

    def create(self, request):
        data = request.data
        pedido = data['pedido']
        data['pedido'] = str(data['pedido'])
        serializer = ContactoProductoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            latest = ContactoProductos.objects.all().last()
            EnviarProducto(serializer.data['asunto'], serializer.data['email'], pedido, serializer.data['nombre'], serializer.data['mail_envio'], latest.id, serializer.data)
            return Response(request.data, status=status.HTTP_201_CREATED)
            #return Response({'error':'serializer invalido'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
