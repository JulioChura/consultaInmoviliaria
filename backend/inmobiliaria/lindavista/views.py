# propiedades/views.py
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Propiedad
from .serializers import PropiedadSerializer

class BuscarPropiedades(APIView):
    def get(self, request):
        # 1. Obtén la consulta enviada desde el frontend
        consulta = request.GET.get('consulta', '')

        if not consulta:
            return Response({'error': 'Debe proporcionar una consulta válida'}, status=400)

        # 2. Divide la consulta en palabras clave
        palabras_clave = consulta.split()  # ['Departamento', 'jacuzzi']

        # 3. Construye un filtro dinámico (intercepta cada término)
        query = Q()
        for palabra in palabras_clave:
            query |= (
                Q(tipo__icontains=palabra) |
                Q(zona__icontains=palabra) |
                Q(descripcion__icontains=palabra)
            )

        # 4. Filtra los resultados usando la consulta dinámica
        propiedades = Propiedad.objects.filter(query)

        # 5. Serializa los resultados
        serializer = PropiedadSerializer(propiedades, many=True)

        # 6. Devuelve la respuesta
        return Response({'resultados': serializer.data}, status=200)
