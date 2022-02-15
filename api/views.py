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
        cuponesToken.append({'codigo': cupon.codigo , 'usado': cupon.usado ,'token': token})

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

        if cupon.usado :
            return Response({'error': True, 'mensaje': 'el cupon de de descuento ya fue canjeado'}, status=status.HTTP_404_NOT_FOUND)
        else:
            cupon.usado = True
            cupon.save()
            cupon = {'valor': cupon.valor, 'mensaje': 'cupon canjeado'}
            return Response(cupon)

    except Cupon.DoesNotExist:
        return Response({'error': True, 'mensaje': 'no existe un cupon con el codigo selecionado'}, status=status.HTTP_404_NOT_FOUND)
        

@api_view(['GET', 'POST'])
def empresa(request):

    if request.method == 'GET':
        print(Empresa.objects.all())
        
        serializer = EmpresaSerializer(Empresa.objects.all(), many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        datos = request.data

     

        serializer = EmpresaSerializer(data=datos)

        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({'error': False, 'mensaje': 'Empresa registrada satifactoriamente'})
        else:
            return Response({'error': True, 'mensaje': 'no se cumplem los parametros para registrar una empresa'})
