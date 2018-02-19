from django.conf.urls import url
from .views import LineaView, ProductoView, DetalleView

urlpatterns = [
    url(r'^linea$', LineaView.as_view()),
    url(r'^producto$', ProductoView.as_view()),
    url(r'^detalle$', DetalleView.as_view())
]