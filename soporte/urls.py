from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.post_list, name='post_landing'),

	path('notificaciones/', views.post_list2, name='post_noti'),
	path('notificaciones/detalles', views.notiFalla, name='noti_detalle'),

	path('asistencia/informatica', views.asisInf, name='asisInf'),

	path('registros1', views.registros1, name="registros1"),
	path('login/', views.login.as_view(), name='login'),

	path('aceptarusers/', views.a_us, name='a_us'),
	path('User?12@#|2aprove?/<int:pk>', views.userAP, name='userAP'),
	path('User?14@#|2aprove?/<int:pk>', views.userNE, name='userNE'),

	path('perfil/<int:pk>/', views.datos_u, name='datos_u'),
	path('datos/<int:pk>/edit/', views.datose, name='datose'),
    path('perfil', views.Datos1, name='datos1'),

    path('opciones_avanzadas', views.opcis_admin, name='opcisAdmin'),
    path('opciones_avanzadas/Opciones-Soporte', views.adm_sop_opcis, name='adm_sop_opcis'),
    path('opciones_avanzadas/Opciones-SoporteForm/<int:pk1>', views.adm_sop_opcisFormF, name='adm_sop_opcisFormF'),
    path('opciones_avanzadas/Opciones-Soporte/<int:pk1>', views.adm_sop_opcis_det, name='adm_sop_opcis_det'),
    path('opciones_avanzadas/Opciones-SoporteForm/Edit/<int:pk1>', views.adm_sop_opcis_detFormF, name='adm_sop_opcis_detFormF'),
    path('opcion?!d#@|reprobar!02091/<int:pk>', views.adm_sop_opcis_detNE, name='adm_sop_opcis_detNE'),


    path('opciones_avanzadas/Opciones-Soporte/Codigo', views.op_codigo, name='op_codigo'),
    path('opciones_avanzadas/Opciones-SoporteForm/Codigo/?8291Create', views.Valid1_codigo, name='Valid1_codigo'),
    path('Acceso_Denegado', views.Error, name='Error1'),


    path('ajax/opcionesP/', views.opcisP, name='ajax_opcisP'),
    path('ajax/valid_usu/', views.validar_usuario, name='ajax_valid_usu'),

]