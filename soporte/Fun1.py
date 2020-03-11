from django.contrib.auth.models import User
from .models import NivelesNum ,P_opci, Datos


def usu_1xnivel (nivel):

	#usu = User.objects.filter(is_active=1).filter(datos_nombre='olwer')
	#usu2 = User.objects.filter()
	#print (nivel.pk)
	usu = User.objects.filter(is_active=1).filter(datos__nivel_usua=nivel.pk).exists()
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
	niveles_interes = [2,3,4,5,6]
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
