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