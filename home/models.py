# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Marca(models.Model):

    #__Marca_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)

    #__Marca_FIELDS__END

    class Meta:
        verbose_name        = _("Marca")
        verbose_name_plural = _("Marca")


class Modelo(models.Model):

    #__Modelo_FIELDS__
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255, null=True, blank=True)

    #__Modelo_FIELDS__END

    class Meta:
        verbose_name        = _("Modelo")
        verbose_name_plural = _("Modelo")


class Procura(models.Model):

    #__Procura_FIELDS__
    odc_contrato = models.CharField(max_length=255, null=True, blank=True)
    codigos_consumibles = models.TextField(max_length=255, null=True, blank=True)
    ceco_oi = models.CharField(max_length=255, null=True, blank=True)
    propiedad = models.CharField(max_length=255, null=True, blank=True)
    solicitado_por = models.CharField(max_length=255, null=True, blank=True)
    proveedor = models.CharField(max_length=255, null=True, blank=True)
    nota_entrega = models.DateTimeField(blank=True, null=True, default=timezone.now)
    fecha_entrega = models.DateTimeField(blank=True, null=True, default=timezone.now)
    valor_historico = models.IntegerField(null=True, blank=True)
    garantia = models.DateTimeField(blank=True, null=True, default=timezone.now)
    fecha_vida_util = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Procura_FIELDS__END

    class Meta:
        verbose_name        = _("Procura")
        verbose_name_plural = _("Procura")


class Codigoconsumible(models.Model):

    #__Codigoconsumible_FIELDS__
    procura = models.ForeignKey(Procura, on_delete=models.CASCADE)
    id = models.CharField(max_length=255, null=True, blank=True)

    #__Codigoconsumible_FIELDS__END

    class Meta:
        verbose_name        = _("Codigoconsumible")
        verbose_name_plural = _("Codigoconsumible")


class Consumible(models.Model):

    #__Consumible_FIELDS__
    procura = models.ForeignKey(Procura, on_delete=models.CASCADE)
    codigo = models.ForeignKey(CodigoConsumible, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=255, null=True, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)
    referencia = models.CharField(max_length=255, null=True, blank=True)
    capacidad = models.IntegerField(null=True, blank=True)
    cantidad = models.IntegerField(null=True, blank=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True, default=timezone.now)
    impresoras_compatibles = models.CharField(max_length=255, null=True, blank=True)

    #__Consumible_FIELDS__END

    class Meta:
        verbose_name        = _("Consumible")
        verbose_name_plural = _("Consumible")



#__MODELS__END
