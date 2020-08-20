from django.contrib import admin
from .models import asistencias_p,estado_soporte_notif, bienes_gob_categoria, Datos,Codigos,NivelesNum, P_opci, P_detal


admin.site.register(P_opci)
admin.site.register(P_detal)
admin.site.register(NivelesNum)
admin.site.register(Codigos)
admin.site.register(Datos)
admin.site.register(bienes_gob_categoria)
admin.site.register(estado_soporte_notif)
admin.site.register(asistencias_p)