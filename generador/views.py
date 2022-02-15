from django.shortcuts import render

from api.models import Empresa


def index(request):
    empresas =  Empresa.objects.all()
    return render(request,'index.html', {'empresas':empresas })


def empresas(request):
      return render(request,'empresas.html')


def cupones(request):
      return render(request,'cupones.html')