from django.shortcuts import render

from generador.models import Cupon

# Create your views here.

def index(request):
    """ cupon = Cupon(empresa='empresa1', codigo='123*+-', valor=10, usado=False)
    cupon.save()"""

    cupones = Cupon.objects.all()

    print(cupones)
    
    return render(request,'index.html')


def empresa(request):

      return render(request,'empresa.html')