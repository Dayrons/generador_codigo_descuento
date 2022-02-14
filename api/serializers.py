 
from rest_framework import serializers
from generador.models import  Cupon
 
class CuponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cupon
        fields = ['id', 'empresa', 'codigo', 'valor', 'usado', ]
        extra_kwargs = {'id': {'required': False}}