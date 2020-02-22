from django.db import models

from django.contrib.auth.models import User

from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.utils import timezone

# Create your models here.

class P_opci(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class P_detal(models.Model):
    p_opci = models.ForeignKey(P_opci, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class unidad2(models.Model):
    nom_unidad = models.CharField(max_length=500)
    def __str__(self):
        return self.nom_unidad

class NivelesNum(models.Model):
    nom_nivel = models.CharField(max_length=200)
    def __str__(self):
        return str(self.nom_nivel)
    

class NivelDet(models.Model):
    usuario = models.OneToOneField('auth.User',on_delete=models.CASCADE, primary_key=True, unique=True)
    nivel_tec = models.BooleanField(default=False)
    nivel_sec = models.BooleanField(default=False)
    nivel_coord_area = models.BooleanField(default=False)

class sub_area(models.Model):
    sub_area_nom = models.CharField(max_length=200)


class Codigos(models.Model):
    codigo = models.IntegerField(unique=True)
    sub_area = models.ForeignKey(P_opci,on_delete=models.CASCADE,null=True)
    cod_area = models.ForeignKey(unidad2, on_delete=models.CASCADE,null=True)
    nivel_num = models.ForeignKey(NivelesNum, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.nivel_num)
        
class Datos(models.Model):
    usuario = models.OneToOneField('auth.User',on_delete=models.CASCADE, primary_key=True, unique=True)
    nombVer = RegexValidator(regex=r'^[a-zA-ZñáéíóúäëïöüÑàèìòù\s]+$', message="Solo letras para el nombre por favor.")
    nombre = models.CharField(validators=[nombVer],max_length=200)
    apellVer = RegexValidator(regex=r'^[a-zA-ZñáéíóúäëïöüÑàèìòù\s]+$', message="Solo letras para el apellido por favor.")
    apellido = models.CharField(validators=[apellVer],max_length=200)
    cedula = models.PositiveIntegerField(unique=True,validators=[MinValueValidator(1000000,message="cedula no valida."), MaxValueValidator(35000000,message="cedula no valida.")])
    email = models.EmailField(null=True)
    fedicion = models.DateTimeField(blank=True, null=True)
    cod_area = models.ForeignKey(unidad2, on_delete=models.CASCADE)
    sub_area = models.ForeignKey(P_opci,on_delete=models.CASCADE,null=True)
    nivel_usua = models.ForeignKey(NivelesNum,on_delete=models.CASCADE,null=True)

    def publish(self):
        self.fedicion = timezone.now()
        self.save()
        #,default=NivelesNum.objects.get(pk=1).pk

    def __str__(self):
        return str(self.usuario_id)+" "+(self.nombre)




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

