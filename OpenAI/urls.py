from django.urls import path
from .views import enviar_mensaje

urlpatterns = [
    path("", enviar_mensaje, name="mensaje"),
]