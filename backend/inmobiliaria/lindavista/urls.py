# lindavista/urls.py
from django.urls import path
from .views import BuscarPropiedades

urlpatterns = [
    path('buscar/', BuscarPropiedades.as_view(), name='buscar_propiedades'),
]
