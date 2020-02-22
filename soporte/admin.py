from django.contrib import admin
from .models import Datos,Codigos,NivelesNum, P_opci, P_detal


admin.site.register(P_opci)
admin.site.register(P_detal)
admin.site.register(NivelesNum)
admin.site.register(Codigos)
admin.site.register(Datos)
