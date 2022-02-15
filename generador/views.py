from django.shortcuts import render

from api.models import Empresa


def index(request):
    empresas =  Empresa.objects.all()
    return render(request,'index.html', {'empresas':empresas })


def empresa(request):
      return render(request,'empresa.html')