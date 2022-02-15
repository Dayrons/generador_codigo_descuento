from api.serializers import CuponSerializer, EmpresaSerializer
from .models import Cupon, Empresa
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random


@api_view(['GET'])
def get(request):

    serializer = CuponSerializer(Cupon.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create(request):

    datos = request.data

    characters = list(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()+{}[]1234567890")

    codigo = ''

    for x in range(24):
        codigo += random.choice(characters)

    datos['codigo'] = codigo

    serializer = CuponSerializer(data=datos)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def empresa(request):
    if request.method == 'GET':
        print(Empresa.objects.all())
        serializer = EmpresaSerializer(Empresa.objects.all(), many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        return Response({'hola': 'mundo'})
