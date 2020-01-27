from django.db import models

from django.contrib.auth.models import User

from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.utils import timezone

# Create your models here.

class unidad2(models.Model):
    nom_unidad = models.CharField(max_length=500)
    def __str__(self):
        return self.nom_unidad

class Niveles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Nivel = models.IntegerField(null=True)

class Datos(models.Model):
    usuario = models.OneToOneField('auth.User',on_delete=models.CASCADE, primary_key=True, unique=True)
    nombVer = RegexValidator(regex=r'^[a-zA-ZñÑ\s]+$', message="Solo letras para el nombre por favor.")
    nombre = models.CharField(validators=[nombVer],max_length=200)
    apellVer = RegexValidator(regex=r'^[a-zA-ZñÑ\s]+$', message="Solo letras para el apellido por favor.")
    apellido = models.CharField(validators=[apellVer],max_length=200)
    cedula = models.PositiveIntegerField(unique=True,validators=[MinValueValidator(1000000,message="cedula no valida."), MaxValueValidator(35000000,message="cedula no valida.")])
    email = models.EmailField(null=True)
    fedicion = models.DateTimeField(blank=True, null=True)
    cod_area = models.ForeignKey(unidad2, on_delete=models.CASCADE)
    cod_nivel = models.IntegerField(null=True)

    def publish(self):
        self.fedicion = timezone.now()
        self.save()

    def __str__(self):
        return str(self.usuario_id)+" "+(self.nombre)


class P_opci(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class P_detal(models.Model):
    p_opci = models.ForeignKey(P_opci, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class sop_notif(models.Model):
    usu_tec = models.ForeignKey('auth.User',on_delete=models.CASCADE, null=True, related_name='Tecnico')
    cod_usu = models.ForeignKey('auth.User',on_delete=models.CASCADE, related_name='Usuario')
    tipo_sop = models.ForeignKey(P_opci,on_delete=models.CASCADE)
    descrip1 =  models.ForeignKey(P_detal,on_delete=models.CASCADE, null=True)
    nombVer = RegexValidator(regex=r'^[a-zA-ZñÑ]+$', message="Solo letras para el nombre por favor.")
    nombre = models.CharField(validators=[nombVer],max_length=200)
    num_pc = models.IntegerField()
    problemaAd = models.CharField(max_length=500)
    estado_sop = models.IntegerField(null=True)

    def __str__(self):
        return self.id

