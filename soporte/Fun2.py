from .Fun1 import usu_1xnivel_areas_o, niveles1_sin_ocupar_area, usu_1xnivel_area, niveles1_sin_ocupar, usu_1xnivel_alt ,usu_1xnivel_sub_area_alt ,usu_1xnivel_sub_area2Form, usu_1xnivel, usu_1xnivel_sub_area
from .models import unidad2
#funciones2
from django.contrib.auth.models import User
from .models import NivelesNum ,P_opci, Datos

def usu_add_1(v_us,Verthandi,usuarios_list):
	for Skuld in v_us:
	    try:
	        datos = Datos.objects.get(pk=Skuld.pk)
	        usuarios_list.append(Skuld)
	        Verthandi.append(datos)
	    except:
	        pass
	return Verthandi,usuarios_list




def a_us_func1():
	usu_nivel = niveles1_sin_ocupar()
	usu_nivel2 = niveles1_sin_ocupar_area()
	Verthandi = []
	niveles_sub_areas = [4,5]
	niveles_no_unicos = [5]
	niveles_areas_o = [7]
	niveles_areas = []
	usuarios_list = []

	for niveles_dispo in usu_nivel:
	    if niveles_dispo.pk in niveles_sub_areas:
	        if niveles_dispo.pk in niveles_no_unicos:
	            #lista de usuarios que se agregaran
	            v_us = User.objects.filter(is_active=0).filter(datos__nivel_usua=niveles_dispo.pk).order_by('id')
	            Verthandi,usuarios_list = usu_add_1(v_us,Verthandi,usuarios_list)
	        else:
	            a12 = usu_1xnivel_sub_area2Form(int(niveles_dispo.pk))
	            #lista de usuarios que se agregaran
	            # En caso de estar vacantes sus puestos
	            for sub_a_dispo in a12:
	                v_us = User.objects.filter(is_active=0).filter(datos__nivel_usua=niveles_dispo.pk).filter(datos__sub_area=sub_a_dispo).order_by('id')
	                Verthandi,usuarios_list = usu_add_1(v_us,Verthandi,usuarios_list)

	    else:
	        if niveles_dispo.pk in niveles_areas_o:
	            areas_t = unidad2.objects.filter().order_by('id')
	            
	            for are in areas_t:
	                a12= usu_1xnivel_areas_o(niveles_dispo.pk,are.pk)
	                if not (a12):
	                    v_us = User.objects.filter(datos__cod_area=are.pk,datos__nivel_usua=niveles_dispo.pk,is_active=0).order_by('id')
	                    Verthandi,usuarios_list = usu_add_1(v_us,Verthandi,usuarios_list)
	                else:
	                    pass
	            #v_us = User.objects.filter(is_active=0,datos__nivel_usua=niveles_dispo.pk).order_by('id')
	            #Verthandi,usuarios_list = usu_add_1(v_us,Verthandi,usuarios_list)
	        else:
	            v_us = User.objects.filter(is_active=0,datos__nivel_usua=niveles_dispo.pk).order_by('id')
	            Verthandi,usuarios_list = usu_add_1(v_us,Verthandi,usuarios_list)
	return usuarios_list,Verthandi
