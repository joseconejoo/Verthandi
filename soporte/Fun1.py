from django.contrib.auth.models import User
from .models import asistencia_personal, asistencias_p, NivelesNum ,P_opci, Datos,unidad2
import datetime

def usu_1xnivel (nivel,area=False):

	#usu = User.objects.filter(is_active=1).filter(datos_nombre='olwer')
	#usu2 = User.objects.filter()
	#print (nivel.pk)
	##usu = None
	##if not area:
	usu = User.objects.filter(is_active=1).filter(datos__nivel_usua=nivel.pk).exists()	
	##else:
	##	print('area',area)
	"""
	usu3 = User.objects.filter(is_active=1).filter(datos__nivel_usua=nivel.pk)
	for usu2 in usu3:
		usu2.is_active = 0
		usu2.save()
	"""
	return (usu)


def usu_1xnivel_alt (nivel):
	usu = User.objects.filter(is_active=1).filter(datos__nivel_usua=nivel.pk).exists()
	return (usu)

def usu_1xnivel_sub_area_alt (nivel,sub_area):
	usu = User.objects.filter(is_active=1).filter(datos__nivel_usua=nivel.pk).filter(datos__sub_area=sub_area.pk).exists()
	return (usu)

def usu_1xnivel_sub_area (nivel):

	#usu = User.objects.filter(is_active=1).filter(datos_nombre='olwer')
	#usu2 = User.objects.filter()
	#print (nivel.pk)
	usu = User.objects.filter(is_active=1).filter(datos__nivel_usua=nivel.pk)
	sub_niveles_cantidad = P_opci.objects.count()
	
	lista_usuarios_areas = []
	for usuarios in usu:
		usuinteres = usuarios.datos.sub_area
		if not (usuinteres in lista_usuarios_areas):
			lista_usuarios_areas.append(usuinteres)
	"""
	usu3 = User.objects.filter(is_active=1).filter(datos__nivel_usua=nivel.pk)
	for usu2 in usu3:
		usu2.is_active = 0
		usu2.save()
	"""
	if sub_niveles_cantidad == len(lista_usuarios_areas):
		resultado = True
	else:
		resultado = False
	return (resultado)


def usu_1xnivel_sub_area2Form (nivel):

	#usu = User.objects.filter(is_active=1).filter(datos_nombre='olwer')
	#usu2 = User.objects.filter()
	#print (nivel.pk)
	
	sub_niveles_cantidad = P_opci.objects.count()
	sub_niveles_lista1 = P_opci.objects.filter().order_by('id')
	sub_niveles_registrar = []

	for niveles in sub_niveles_lista1:
		usu = User.objects.filter(is_active=1).filter(datos__nivel_usua=nivel).filter(datos__sub_area=niveles.pk)
		if not(usu):
			sub_niveles_registrar.append(niveles)

	"""
	for usuarios in usu:
		usuinteres = usuarios.datos.sub_area
		if not (usuinteres in lista_usuarios_areas):
			lista_usuarios_areas.append(usuinteres)
	"""


	"""
	usu3 = User.objects.filter(is_active=1).filter(datos__nivel_usua=nivel.pk)
	for usu2 in usu3:
		usu2.is_active = 0
		usu2.save()
	"""

	return (sub_niveles_registrar)



"""
asdasdasd
"""

def niveles1_sin_ocupar():
	usu_niv2 = NivelesNum.objects.filter().order_by('id')
	usu_nivel = []
	niveles_interes = [2,3,4,5,6,7]
	#HACER VALIDACION DEL 7 POR AREA
	niveles_sub_areas = [4]
	niveles_no_unicos = [5,6,7]
	niveles_areas_o = []

	for x in usu_niv2:
	    if x.pk in niveles_interes:
	        if (x.pk) in niveles_sub_areas:
	            a12 = usu_1xnivel_sub_area(x)
	            if not(a12):
	                x.nombre = x.nom_nivel
	                usu_nivel.append(x)
	            else:
	            	pass
	        elif (x.pk) in niveles_no_unicos:
	        	if (x.pk) in niveles_areas_o:
	        		pass
	        	else:
	        		x.nombre = x.nom_nivel
	        		usu_nivel.append(x)

	        else:
	            a12 = usu_1xnivel(x)
	            if not(a12):
	                x.nombre = x.nom_nivel
	                usu_nivel.append(x)
	return usu_nivel



def usu_1xnivel_area (nivel,area):

	usu = User.objects.filter(datos__cod_area=area.pk,datos__nivel_usua=nivel.pk,is_active=1).exists()
	"""
	usu3 = User.objects.filter(is_active=1).filter(datos__nivel_usua=nivel.pk)
	for usu2 in usu3:
		usu2.is_active = 0
		usu2.save()
	"""
	return (usu)


def niveles1_sin_ocupar_area():
	usu_niv2 = NivelesNum.objects.filter().order_by('id')
	usu_nivel = []
	niveles_interes = [7]
	#HACER VALIDACION DEL 7 POR AREA
	niveles_sub_areas = [4]
	niveles_no_unicos = [5,6]
	for x in usu_niv2:
	    if x.pk in niveles_interes:
	        if (x.pk) in niveles_sub_areas:
	            a12 = usu_1xnivel_sub_area(x)
	            if not(a12):
	                x.nombre = x.nom_nivel
	                usu_nivel.append(x)
	            else:
	            	pass
	        elif (x.pk) in niveles_no_unicos:
	        	x.nombre = x.nom_nivel
	        	usu_nivel.append(x)
	        else:
	            a12 = usu_1xnivel(x)
	            if not(a12):
	                x.nombre = x.nom_nivel
	                usu_nivel.append(x)
	return usu_nivel
def usu_1xnivel_areas_o(nivel,area):
	usua = User.objects.filter(datos__cod_area=area,datos__nivel_usua=nivel,is_active=1).exists()
	return usua



def asis_re(empleados,hoy,x2,hactual2):
	for emple in empleados:
		if hactual2 > x2:
			if not(asistencia_personal.objects.filter(n_asistencia=asistencias_p.objects.filter(fecha_a=hoy)[0],n_empleado=emple)):
			    asistencia_personal.objects.create(n_asistencia=asistencias_p.objects.filter(fecha_a=hoy)[0],n_empleado=emple,asistente=False)



def obten_tiem():
	hoy = datetime.datetime.today()
	hoy2 = datetime.date.today()
	hactual = str(hoy)[11:]
	hactual2=str(hactual)[:8]
	x = '07:30:00'
	x2 = '08:30:00'
	return hoy,hoy2,hactual,hactual2,x,x2