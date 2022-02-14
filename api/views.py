from django.shortcuts import render
from api.serializers import CuponSerializer
from generador.models import Cupon

from rest_framework import viewsets
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response




class CuponViewSet(viewsets.ModelViewSet):
    queryset = Cupon.objects.all()
    serializer_class = CuponSerializer
     
