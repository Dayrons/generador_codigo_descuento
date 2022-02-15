from rest_framework import status
from api.serializers import CuponSerializer, EmpresaSerializer
from .models import Cupon, Empresa
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random
import jwt


@api_view(['GET'])
def get(request):
    
    cupones = Cupon.objects.all()
    cuponesToken = []
    for  cupon in cupones:
        token = jwt.encode({"id": cupon.id }, cupon.codigo, algorithm="HS256")
        cuponesToken.append({'codigo': cupon.codigo , 'token': token})

    return Response(cuponesToken)



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


@api_view(['POST'])
def cajear(request):

    codigo = request.data['codigo']
    

    try:
        cupon = Cupon.objects.get(codigo=codigo)

        if cupon.usado:
            serializer = CuponSerializer(cupon, many=False)
            datos = request.data
            token = jwt.decode(datos['token'], datos['codigo'], algorithms=["HS256"])
            return Response(serializer.data)
        else:
            return Response({'error': True, 'mensaje': 'el cupon de de descuento ya fue canjeado'}, status=status.HTTP_404_NOT_FOUND)

        
    except Cupon.DoesNotExist:
        return Response({'error': True, 'mensaje': 'no existe un cupon con el codigo selecionado'}, status=status.HTTP_404_NOT_FOUND)
        

        

@api_view(['GET', 'POST'])
def empresa(request):

    if request.method == 'GET':
        print(Empresa.objects.all())
        serializer = EmpresaSerializer(Empresa.objects.all(), many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        return Response({'hola': 'mundo'})
