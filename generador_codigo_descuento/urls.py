"""generador_codigo_descuento URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from generador import  views
# from rest_framework import routers

from api import views as api

""" router = routers.DefaultRouter()

router.register(r'cupones', api.getData,  basename='api') """

urlpatterns = [
    path('', views.index),
    path('empresas', views.empresas),
    path('cupones', views.cupones),
    path('api/v1/cupones', api.get),
    path('api/v1/cupones/create', api.create),
    path('api/v1/cupones/canjear', api.cajear),
    path('api/v1/empresa', api.empresa),
    # path('admin/', admin.site.urls),
]
