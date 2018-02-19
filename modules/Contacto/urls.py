from django.conf.urls import url
from .views import ContactoView, ContactoProductoView

urlpatterns = [
    url(r'^contacto/', ContactoView.as_view()),
    url(r'^cproducto/', ContactoProductoView.as_view()),
]