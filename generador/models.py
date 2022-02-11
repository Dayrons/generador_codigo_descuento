from django.db import models

from django.db.models.fields import CharField, BooleanField, IntegerField


class Cupon(models.Model):
    empresa = CharField(max_length=100)
    codigo = CharField(max_length=100)
    valor = IntegerField()
    usado = BooleanField()
