from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.utils import timezone

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse, FileResponse

from .models import estado_soporte_notif, sop_notif_mes, bie_gob_bienes, NivelesNum,Codigos,unidad2 ,P_opci, sop_notif, P_detal, NivelDet, Datos
from django.contrib.auth.models import User

from .forms import sop_notif_mesF, report_usu_areaF, Datos_per_infoF ,CodigosF ,DatosRF ,P_detalF ,P_opciF,AuthenticationForm, sop_notifF, DatosF

from .Com import migracion_bienes_g_bienes, migracion_bienes_gobs, test_velocidad, migracion
from .Fun1 import usu_1xnivel_areas_o, niveles1_sin_ocupar_area, usu_1xnivel_area, niveles1_sin_ocupar, usu_1xnivel_alt ,usu_1xnivel_sub_area_alt ,usu_1xnivel_sub_area2Form, usu_1xnivel, usu_1xnivel_sub_area
from .Fun2 import usu_add_1

from django.contrib import messages

import random

from django.contrib.auth.views import LoginView
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)


# Create your views here.
def registros1(request):
    formlistoption = None
    formlistoption = unidad2.objects.filter().order_by('id')
    """
    posts123 = User.objects.filter(username='kukux2').order_by('pk')
    x123 = User.objects.get(username='kukux2')
    print (x123)
    x123.is_active=True
    x123.is_staff=True
    x123.is_superuser=False
    x123.save()
    
    for x in range(0,10):
        print (x==0)

    User.objects.create_user(username='parapeto2',password='123654ASD')
    """
    if request.method == "POST":
        foxr = UserCreationForm(request.POST)
        form2= DatosRF(request.POST)
        #print (request.POST.get('codigo'))
        if foxr.is_valid() and form2.is_valid():
            #codd = request.POST.get('codigo')
            post = foxr.save(commit=False)
            #cod_usu_n = get_object_or_404(Codigos, codigo=codd)
            #numero_nivel = int(str(cod_usu_n.nivel_num.pk))
            numero_nivel = request.POST.get('nivel_usua')
            #cod_usu_n2 = get_object_or_404(NivelesNum, pk=numero_nivel)
            #1cod_usu_n2 = NivelesNum.objects.get(pk=numero_nivel)
            post.is_active=0
            post2=form2.save(commit=False)

            lista_num =[1,2,3,4,5]
            if numero_nivel in lista_num:
                post2.cod_area = unidad2.objects.get(pk=16)

            lista_coord = [2]
            if numero_nivel in lista_coord:
                post.is_superuser=True
            post.save()
            usuario1 = User.objects.get(pk=post.pk)
            post2.usuario=usuario1
            
            post2.save()
            #Niveles.objects.create(user=User.objects.get(id=post.pk))
            activate = True
            messages.success(request, 'Registro Realizado exitosamente, Debe esperar la Aprobacion del Director')
            return redirect('login')
    else:
        foxr = UserCreationForm()
        form2 = DatosRF()
        
        """
        for x in range(0,1):
            print (formlistoption[0].id)
        """
    return render(request, 'registros1.html', {'form': foxr, "form2":form2, 'formOpti':formlistoption})


class login(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def dispatch(self, request, *args, **kwargs):
        #migracion()
        if request.user.is_authenticated!=True:
            if self.redirect_authenticated_user and self.request.user.is_authenticated:
                redirect_to = self.get_success_url()
                return HttpResponseRedirect(redirect_to)
            return super().dispatch(request, *args, **kwargs)

        else:
            redirect_to = self.get_success_url()
            return HttpResponseRedirect(redirect_to)
    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs



def datos_uRed(request,pk):
    usuarioCoord = User.objects.filter(datos__cod_area=pk,datos__nivel_usua=7,is_active=1)
    if (usuarioCoord[0]):
        return redirect ('datos_u',pk=usuarioCoord[0].pk)


def post_list(request):
    #print (request.user.niveles.Nivel)
    posts=None
    return redirect('login')
    return render(request, 'post_list.html', {'posts': posts})

def post_list2(request):
    #print (request.user.niveles.Nivel)
    #test_velocidad()
    """
    asd = unidad2.objects.filter()
    for x in asd:
        print (x)
    """
    #migracion_bienes_g_bienes()
    #bie_gob_bienes.objects.all().delete()
    posts=None
    notificacion_f = False
    uservalidNotif = False
    if request.method == "POST":
        form = sop_notifF(request.POST)
        if form.is_valid():

            post = form.save(commit=False)
            post.cod_usu = request.user
            #post.fedicion = timezone.now()
            post.fecha_pub = timezone.now()
            numero_d_pc = post.num_pc
            num_d_pc = bie_gob_bienes.objects.filter(codigo_e=numero_d_pc)[0]
            post.nombre_e = num_d_pc.nombre
            post.ubicacion_e = num_d_pc.idunidad.nom_unidad

            post.save()
            messages.success(request,'Notificación enviada exitosamente')
            return redirect('post_noti')
    else:
        Reportador = None
        try:
            Reportador = request.user.report_usu_area.nivel_usua
        except:
            pass
        if not( Reportador ):
            form = None
        else:
            form = sop_notifF()
        niveles_ver_reports = [1,2,4,5]
        if (Datos.objects.filter(pk=request.user.pk).exists()):
            if request.user.datos.nivel_usua.pk in niveles_ver_reports:
                uservalidNotif = True
                notificacion_f = sop_notif.objects.filter(tipo_sop_id__isnull=True)
                notificaciom_f = None
        notif_num_cant = []
        #sacando la informacion para mostrar del numero de publicaciones
        for x in estado_soporte_notif.objects.filter():
            informacion = []
            sop_count = sop_notif.objects.filter(estado_sop=x.pk).count()
            sop_ult = sop_notif.objects.filter(estado_sop=x.pk).order_by('-id')[:1]
            informacion.append(x.nombre)
            informacion.append(sop_count)
            informacion.append(x.pk)
            informacion.append(sop_ult)
            notif_num_cant.append(informacion)
        informacion = []
        sop_count = sop_notif.objects.filter(estado_sop__isnull=True,tipo_sop__isnull=False).count()
        sop_ult = sop_notif.objects.filter(estado_sop__isnull=True,tipo_sop__isnull=False).order_by('-id')[:1]
        informacion.append('Por atender')
        informacion.append(sop_count)
        informacion.append(4)
        informacion.append(sop_ult)
        notif_num_cant.append(informacion)

    return render(request, 'post_list2.html', {'notif_n_cant':notif_num_cant,'uservalidNotif':uservalidNotif,'notificaciones_f':notificacion_f,'posts': posts, 'form': form})

def notif_results(request,pk):
    #trabj1
    notif_atend = [4]
    uservalidNotif = True
    sop_notifs = None
    sop_notifs_nom = None
    if not (pk in notif_atend):
        sop_notifs = sop_notif.objects.filter(estado_sop=pk).order_by('-id')
        sop_notifs_nom = estado_soporte_notif.objects.get(pk=pk)
    else:
        sop_notifs = sop_notif.objects.filter(estado_sop__isnull=True,tipo_sop__isnull=False).order_by('-id')
        sop_notifs_nom = 'Por atender'
    return render(request, 'post_list2_notifs.html', {'sop_notifs_nom':sop_notifs_nom,'uservalidNotif':uservalidNotif,'notifs':sop_notifs})


def a_us(request):
    if request.user.is_authenticated==True:
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


        return render(request, 'v_us2.html', {'v_us': usuarios_list,'datos':Verthandi})
    
    else:
        return HttpResponseRedirect("/")



def userAP(request, pk):
    if request.user.is_superuser:
        niveles_interes = [2,3]
        niveles_sub_areas = [4]
        Verthandi = get_object_or_404(User, pk=pk)
        nombr = Verthandi.username
        #print (Verthandi['is_active'])
        usuarios = User.objects.filter()
        if Verthandi.datos.nivel_usua.pk in niveles_sub_areas:
            asd = usu_1xnivel_sub_area_alt(Verthandi.datos.nivel_usua,Verthandi.datos.sub_area)
            if not(asd):
                Verthandi.is_active = True
                Verthandi.save()
                messages.success(request, 'Usuario '+str(nombr)+' Aprobado exitosamente')
            else:
                messages.error(request, 'Usuario '+str(nombr)+' Ya existe un usuario con este cargo')

        elif Verthandi.datos.nivel_usua.pk in niveles_interes:
            asd = usu_1xnivel_alt(Verthandi.datos.nivel_usua)
            if not(asd):
                Verthandi.is_active = True
                Verthandi.save()
                messages.success(request, 'Usuario '+str(nombr)+' Aprobado exitosamente')

            else:
                messages.error(request, 'Usuario '+str(nombr)+' Ya existe un usuario con este cargo')

        else:
            Verthandi.is_active = True
            Verthandi.save()
            messages.success(request, 'Usuario '+str(nombr)+' Aprobado exitosamente')


        return redirect('a_us')

    else:
        return redirect ("/")


def userNE(request, pk):
    if request.user.is_superuser:
        Verthandi = get_object_or_404(User, pk=pk)
        nombr = Verthandi.username
        Verthandi.delete()
        messages.success(request, 'Usuario '+str(nombr)+' Eliminado exitosamente')
        return redirect('a_us')

    else:
        return redirect ("/")

def userDES(request, pk):
    if request.user.is_superuser:
        Verthandi = get_object_or_404(User, pk=pk)
        nombr = Verthandi.username
        Verthandi.is_active = False
        Verthandi.save()
        messages.success(request, 'Usuario '+str(nombr)+' Deshabilitado exitosamente')
        return redirect('datos_u', pk=pk)

    else:
        return redirect ("/")

def userHAB(request, pk):
    if request.user.is_superuser:
        niveles_interes = [2,3]
        niveles_sub_areas = [4]
        Verthandi = get_object_or_404(User, pk=pk)
        nombr = Verthandi.username
        #print (Verthandi['is_active'])
        usuarios = User.objects.filter()
        if Verthandi.datos.nivel_usua.pk in niveles_sub_areas:
            asd = usu_1xnivel_sub_area_alt(Verthandi.datos.nivel_usua,Verthandi.datos.sub_area)
            if not(asd):
                Verthandi.is_active = True
                Verthandi.save()
                messages.success(request, 'Usuario '+str(nombr)+' Aprobado exitosamente')
            else:
                messages.error(request, 'Usuario '+str(nombr)+' Ya existe un usuario con este cargo')

        elif Verthandi.datos.nivel_usua.pk in niveles_interes:
            asd = usu_1xnivel_alt(Verthandi.datos.nivel_usua)
            if not(asd):
                Verthandi.is_active = True
                Verthandi.save()
                messages.success(request, 'Usuario '+str(nombr)+' Aprobado exitosamente')

            else:
                messages.error(request, 'Usuario '+str(nombr)+' Ya existe un usuario con este cargo')

        else:
            Verthandi.is_active = True
            Verthandi.save()
            messages.success(request, 'Usuario '+str(nombr)+' Aprobado exitosamente')


        return redirect('datos_u', pk=pk)

    else:
        return redirect ("/")

def datos_u(request, pk):

    try:
        dat=Datos.objects.get(pk=pk)
        Verthandi=User.objects.get(pk=pk)
        allow = False
        if request.user.is_superuser:
            if not (request.user.pk == Verthandi.pk) and not(Verthandi.datos.nivel_usua.pk == 1):
                allow = True
        datos = get_object_or_404(Datos, pk=pk)
        return render(request, 'datos_u.html', {'permisos_adm':allow,'datos': datos,'dat': dat,'usuario1':Verthandi})

    except:
        if request.method == "POST":
            form = DatosF(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.usuario = User.objects.get(id=pk)
                post.fedicion = timezone.now()
                post.save()

                return redirect('datos_u', pk=post.pk)
        else:
            form = DatosF()
        return render(request, 'datose.html', {'form': form})


def datose(request, pk):
    post = get_object_or_404(Datos, pk=pk)
    if request.method == "POST":
        form = DatosF(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.usuario = request.user
            post.fedicion = timezone.now()
            post.save()
            return redirect('datos_u', pk=post.pk)
    else:
        form = DatosF (instance=post)
    return render(request, 'datose.html', {'form': form})

def Datos1(request):
    try:
        if request.user.is_superuser or (request.user.datos.nivel_usua):
            pass
        else:
            return redirect('post_noti')
    except:
        return redirect('post_noti')
    if request.method == "POST":
        form = DatosF(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.usuario = request.user
            #Actualizar Createsuperuser y eliminar esto
            if (request.user.is_superuser):
                post.cod_area = unidad2.objects.get(pk=1)

            post.fedicion = timezone.now()
            post.save()
            return redirect('datos_u', pk=post.pk)
    else:
        if Datos.objects.filter(usuario_id=request.user.pk).exists():
            return redirect('datos_u', pk=request.user.pk)
        form = DatosF()
    return render(request, 'datose.html', {'form': form})


def notiFalla(request,pk):
    if request.method == "POST":
        notif = get_object_or_404(sop_notif,pk=pk)
        form = sop_notif_mesF(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.sop_notif_tick = sop_notif.objects.get(pk=pk)
            post.usu_tec = request.user
            if not(post.tipo_sop == notif.tipo_sop):
                notif.tipo_sop = post.tipo_sop
                notif.save()
            else:
                post.tipo_sop = None
            if not(post.estado_sop == notif.estado_sop):
                notif.estado_sop = post.estado_sop
                notif.save()
            else:
                post.estado_sop = None
            """
            if (request.user.is_superuser):
                post.cod_area = unidad2.objects.get(pk=1)
            """
            post.fecha_pub = timezone.now()
            post.save()
            return redirect('noti_detalle', pk=pk)
    else:
        notif = get_object_or_404(sop_notif,pk=pk)
        nivel_atender = [5]
        coord = False
        #coordinador del usuario
        atender = False
        form = None
        diagnostico = False
        solucionado = False
        solucionadosList = [1,3]
        mensajes = sop_notif_mes.objects.filter(sop_notif_tick=pk)
        if (notif.estado_sop):
            if notif.estado_sop.pk in solucionadosList:
                solucionado = True
        if (notif.tipo_sop):
            diagnostico = True

        try:
            if request.user.datos.nivel_usua.pk in nivel_atender:
                form = sop_notif_mesF()
                if notif.tipo_sop:
                    form.initial['tipo_sop'] = notif.tipo_sop
                if notif.estado_sop:
                    form.initial['estado_sop'] = notif.estado_sop

                atender = True

        except:
            pass

        if User.objects.filter(datos__cod_area=pk,datos__nivel_usua=7,is_active=1).exists():
            coord=True
        return render(request, 'notiF_detalle.html', {'solucionado':solucionado,'mensajes':mensajes,'diagnostic':diagnostico,'form':form,'atend':atender,'noti_det':notif,'coord':coord})

def asisInf(request):
    return render(request, 'asisInf.html')

def opcisP(request):
    #Ajax
    tipo_sop_id = request.GET.get('tipo_sop')
    p_detal = P_detal.objects.filter(p_opci_id=tipo_sop_id).order_by('nombre')
    return render(request, 'old2/opciones.html', {'posts': p_detal})

def validar_usuario(request):
    #Ajax
    username = request.GET.get('username', None)
    usu_ex = User.objects.filter(username__exact=username).exists()
    data = {
        'usuario_tomado': usu_ex
    }
    return JsonResponse(data)

def validar_nivel_usuario(request):
    #Ajax3 sub_nivel usuario
    nivel_usuario_r = request.GET.get('nivel_usua_v', None)
    niveles_sub_areas = [4,5]
    niveles_no_unicos = [5]
    lista_sub_areas_dispo = []

    """
    nivel_ex = False

    if int(nivel_usuario_r) in nivel_sub_area:
        nivel_ex = True

    data = {
        'nivel_sub_area': nivel_ex
    }
    return JsonResponse(data)
    """
    a12 = None
    nivel_usuario_r = int(nivel_usuario_r)
    if (nivel_usuario_r) in niveles_sub_areas:
        if (nivel_usuario_r) in niveles_no_unicos:
            a12 = P_opci.objects.filter().order_by('id')
        else:
            a12 = usu_1xnivel_sub_area2Form(int(nivel_usuario_r))
    else:
        niveles_sub = None

    return render(request, 'old2/opciones.html', {'posts': a12})
    



def aj_opcis_nivel(request):
    #Ajax4 opciones niveles
    cod_area_get = request.GET.get('num_nivel', None)
    usu_niv = None
    try:
        usu_niv = unidad2.objects.get(nom_unidad__exact=cod_area_get)
    except:
        pass
    area_interes = [16]
    niveles_interes = [2,3,4,5]
    niveles_interes_areas = [7]
    niveles_sub_areas = [4]
    niveles_no_unicos = [5]
    niveles_areas_no_unicos = [8]
    usu_nivel = []
    if usu_niv:
        if usu_niv.pk in area_interes:
            usu_niv2 = NivelesNum.objects.filter().order_by('id')
            for x in usu_niv2:
                if x.pk in niveles_interes:
                    if x.pk in niveles_sub_areas:
                        a12 = usu_1xnivel_sub_area(x)
                        if not(a12):
                            x.nombre = x.nom_nivel
                            usu_nivel.append(x)
                        else:
                            pass
                    elif x.pk in niveles_no_unicos:
                        x.nombre = x.nom_nivel
                        usu_nivel.append(x)
                    else:
                        a12 = usu_1xnivel(x)
                        if not(a12):
                            x.nombre = x.nom_nivel
                            usu_nivel.append(x)
                        else:
                            pass
                else:
                    pass
        else:
             usu_niv2 = NivelesNum.objects.filter().order_by('id')
             for x in usu_niv2:
                 if x.pk in niveles_interes_areas:
                     if x.pk in niveles_no_unicos:
                         x.nombre = x.nom_nivel
                         usu_nivel.append(x)
                     else:
                        a12 = usu_1xnivel_area(x,usu_niv)
                        if not (a12):
                            print (a12)
                            x.nombre = x.nom_nivel
                            usu_nivel.append(x)
                        else:
                            pass
                        
                 
    """
    data = {
        'usuario_tomado': usu_ex
    }
    """
    print (usu_nivel)
    return render(request, 'old2/opciones.html', {'posts': usu_nivel})

def opcis_admin(request):
    posts=None

    return render(request, 'opciones_admin.html', {'posts': posts})

def adm_sop_opcis(request):
    opcionesSop = P_opci.objects.filter().order_by('id')
    form = None
    if (request.user.is_superuser):
        form = P_opciF()
    return render(request, 'adm_sop_opcis.html', {'opcionesS': opcionesSop,'form':form})

def adm_sop_opcisFormF(request,pk1):
    if request.method == "POST":
        if (request.user.is_superuser):
            pk2 = get_object_or_404(P_opci, pk=pk1)
            form = P_opciF(request.POST, instance=pk2)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('adm_sop_opcis')

    else:
        if (request.user.is_superuser):
            form = P_opciF(instance=pk1)
            print(1,"\n1\n")

def adm_sop_opcis_det(request,pk1):
    opcionesSop = P_detal.objects.filter(p_opci=pk1).order_by('id')
    form = None
    if (request.user.is_superuser):   
        form = P_detalF()
    return render(request, 'adm_sop_opcisDetal.html', {'opcionesS': opcionesSop,'form':form})

def adm_sop_opcis_detFormF(request,pk1):
    if request.method == "POST":
        if (request.user.is_superuser):
            pk2 = get_object_or_404(P_detal, pk=pk1)
            redirec = pk2.p_opci.pk
            form = P_detalF(request.POST, instance=pk2)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('adm_sop_opcis_det',pk1=redirec)

    else:
        if (request.user.is_superuser):
            form = P_detalF(instance=pk1)
def adm_sop_opcis_detNE(request, pk):
    if request.user.is_superuser:
        elim_opci_detal = get_object_or_404(P_detal, pk=pk)
        redirec = elim_opci_detal.p_opci.pk
        elim_opci_detal.delete()
        return redirect('adm_sop_opcis_det',pk1=redirec)

    else:
        return redirect ("/")

def op_codigo(request):
    post = Codigos.objects.order_by('id')
    post22 = NivelesNum.objects.order_by('id')
    post2 = NivelesNum.objects.order_by('id')#[1:]
    post3 = P_opci.objects.order_by('id')
    sub_area = P_opci.objects.filter().order_by('id')
    niveles_sub_areas = [4]
    niveles_interes = [2,3,4]
    lista_codigos = []

    for n_numeros in post2:
        if n_numeros.pk in niveles_interes:
            if n_numeros.pk in niveles_sub_areas:
                lis_codigo = []
                lis_sub = []
                for x in sub_area:
                    x123 = NivelesNum.objects.get(pk=n_numeros.pk)
                    x123.sub_area = x
                    x123.sub_areapk = x.pk
                    lista_codigos.append(x123)
                for x in Codigos.objects.filter(nivel_num=post22[n_numeros.pk-1]):
                    lis_codigo.append(int(str(x.pk)))
                #print (lis_codigos)

            else:
                if Codigos.objects.filter(nivel_num=post22[n_numeros.pk-1]).exists():
                    codigo = Codigos.objects.get(nivel_num=post22[n_numeros.pk-1])
                    n_numeros.codigo1 = codigo.codigo
                    n_numeros.codigo1pk = codigo.pk
                else:
                    n_numeros.sub_areapk = 0
                lista_codigos.append(n_numeros)


    #post.delete()
    return render(request, 'valids.html', {'code': lista_codigos,'sub_a':post3})

def Valid1_codigo(request,pk,pk1=0):
    niveles_sub_areas = [4]
    if request.user.is_superuser or request.user.is_staff:
        codigo = NivelesNum.objects.get(pk=pk)
        print (codigo)
        if request.method == "POST":
            if pk1 == 0:
                if Codigos.objects.filter(nivel_num=pk).exists():
                    return redirect('op_codigo')
                    #verifica que no haya otro codigo en el lugar
                else:
                    while True:
                        x12 = random.randint(1000, 9999)
                        if not Codigos.objects.filter(codigo=x12).exists() :
                            nivel1 = NivelesNum.objects.get(pk=pk)
                            Codigos.objects.create(codigo=x12,nivel_num=nivel1)
                            return redirect('op_codigo')
            else:
                lis_codigos = []
                if Codigos.objects.filter(nivel_num=pk).exists():
                    lis_codigos.append(Codigos.objects.filter(nivel_num=pk))
                    #HACER CORREGIR ESTA PARTE, VERIFICACION NO FUNCIONA
                    if not Codigos.objects.filter(sub_area=pk1) in lis_codigos:
                        while True:
                            x12 = random.randint(1000, 9999)
                            if not Codigos.objects.filter(codigo=x12).exists() :
                                nivel1 = NivelesNum.objects.get(pk=pk)
                                nivel2 = P_opci.objects.get(pk=pk1)
                                Codigos.objects.create(codigo=x12,nivel_num=nivel1,sub_area=nivel2)
                                return redirect('op_codigo')

                    else:
                        return redirect('op_codigo')
                else:
                    while True:
                        x12 = random.randint(1000, 9999)
                        if not Codigos.objects.filter(codigo=x12).exists() :
                            nivel1 = NivelesNum.objects.get(pk=pk)
                            nivel2 = P_opci.objects.get(pk=pk1)
                            Codigos.objects.create(codigo=x12,nivel_num=nivel1,sub_area=nivel2)
                            return redirect('op_codigo')



        else:
            form = ValidF()
        return render(request, 'valid.html', {'form': form})
    else:
        return redirect('Error1')


def Del1_codigo(request,pk):
    codigo = Codigos.objects.get(pk=pk)
    codigo.delete()
    return redirect('op_codigo')


def Error(request):
    return render(request, "Negado.html")


def personal_inf(request):
    posts=None
    niveles_v = NivelesNum.objects.filter().order_by('id')
    sub_area = P_opci.objects.filter().order_by('id')
    niveles_interes = [1,2,3,4]
    niveles_sub_areas = [4]
    niveles_lista = []
    """
    usuarios = []
    usuarios2 = User.objects.filter().order_by('id')
    for x in usuarios2:
        usuarios.append(x)
    usuarios_f = []
    usuarios_sub = []
    usuarios_i = []"""
    """
    for x in usuarios:
        try:
            if x.datos.nivel_usua.pk in niveles_interes:
                if not (x.datos.nivel_usua.pk in usuarios_f) :
                    usuarios_i.append(x)
                    usuarios_f.append(x.datos.nivel_usua.pk)
                elif (x.datos.nivel_usua.pk in niveles_sub_areas) and (x.datos.sub_area in usuarios_sub):
                    pass

        except:
            pass
    #usuarios arriba filtrado

    print (usuarios_i)
    """
    for x in niveles_v:
        if x.pk in niveles_interes:
            if x.pk in niveles_sub_areas:
                for y in sub_area:
                    x123 = NivelesNum.objects.get(pk=x.pk)
                    x123.sub_area = str(y.nombre)
                    usu = User.objects.filter(is_active=1).filter(datos__nivel_usua=x.pk).filter(datos__sub_area=y.pk)
                    if usu:
                        x123.encargado = usu[0]
                        niveles_lista.append(x123)
                    else:
                        niveles_lista.append(x123)
            else:
                agregado = False
                usu = User.objects.filter(is_active=1).filter(datos__nivel_usua=x.pk)
                if usu:
                    agregado = True
                    x.encargado = usu[0]
                    niveles_lista.append(x)
                if not (agregado):
                    niveles_lista.append(x)

    
    """
    for x in usuarios:
        for y in range (0, (len(usuarios))-1):
            usuario_ar = usuarios[y+1]
            usu_act = usuarios [y]
            try:
                if (usu_act.datos.nivel_usua.pk) > (usuario_ar.datos.nivel_usua.pk):
                    buff = usuario_ar
                    usuarios[y+1] = usuarios[y]
                    usuarios[y] = buff
            except:
                pass
    """
    return render(request, 'personal_inf.html', {'niveles':niveles_lista})

def registros_personal_inf(request):
    formlistoption = None
    formlistoption = unidad2.objects.filter().order_by('id')
    if request.method == "POST":
        foxr = UserCreationForm(request.POST)
        form2= Datos_per_infoF(request.POST)
        #print (request.POST.get('codigo'))
        if foxr.is_valid() and form2.is_valid():
            #codd = request.POST.get('codigo')
            post = foxr.save(commit=False)
            #cod_usu_n = get_object_or_404(Codigos, codigo=codd)
            #numero_nivel = int(str(cod_usu_n.nivel_num.pk))
            numero_nivel = 6
            #cod_usu_n2 = get_object_or_404(NivelesNum, pk=numero_nivel)
            #1cod_usu_n2 = NivelesNum.objects.get(pk=numero_nivel)
            post.is_active=0
            post2=form2.save(commit=False)

            lista_num =[1,2,3,4,5,6]
            if numero_nivel in lista_num:
                post2.cod_area = unidad2.objects.get(pk=16)

            lista_coord = [2]
            if numero_nivel in lista_coord:
                post.is_superuser=True
            post.save()
            post2.nivel_usua = NivelesNum.objects.get(pk=numero_nivel)
            usuario1 = User.objects.get(pk=post.pk)
            post2.usuario=usuario1
            
            post2.save()
            #Niveles.objects.create(user=User.objects.get(id=post.pk))
            activate = True
            messages.success(request, 'Registro realizado exitosamente, debe esperar la aprobación del Director')
            return redirect('personal_inf_v')
    else:
        foxr = UserCreationForm()
        form2 = Datos_per_infoF()
        
        """
        for x in range(0,1):
            print (formlistoption[0].id)
        """
    return render(request, 'registros1_personal.html', {'form': foxr, "form2":form2, 'formOpti':formlistoption})


def personal_inf_v(request):
    if request.user.is_authenticated==True:

        v_us = User.objects.filter(is_active=1).filter(datos__nivel_usua=6).order_by('id')
        Verthandi=[]
        for Skuld in v_us:
            try:
                datos = Datos.objects.get(pk=Skuld.pk)
                Verthandi.append(datos)
            except:
                pass

        return render(request, 'v_us2_personal.html', {'v_us': v_us,'datos':Verthandi})
    
    else:
        return HttpResponseRedirect("/")

def usuarioReport(request):
    Verthandi=User.objects.get(pk=request.user.pk)
    #print (request.user.datos.nivel_usua,request.user.datos.nivel_usua.pk)
    usu_reportador = User.objects.filter(report_usu_area__cod_area=request.user.datos.cod_area.pk,report_usu_area__nivel_usua=8)
    #print (usu_reportador,usu_reportador[0])
    allow = False
    if usu_reportador:
        datos = get_object_or_404(User, pk=usu_reportador[0].pk)
    else:
        datos = False
    """
    if request.user.is_superuser:
        if not (request.user.pk == Verthandi.pk) and not(Verthandi.datos.nivel_usua.pk == 1):
            allow = True
    """
    return render(request, 'datos_reportador.html', {'permisos_adm':allow,'datos': datos,'usuario1':Verthandi})

def usuarioReportRegis(request):
    formlistoption = None
    formlistoption = unidad2.objects.filter().order_by('id')
    usu_reportador = User.objects.filter(report_usu_area__cod_area=request.user.datos.cod_area.pk,report_usu_area__nivel_usua=8).exists()
    if not (usu_reportador):
        if request.method == "POST":
            foxr = UserCreationForm(request.POST)
            form2= report_usu_areaF(request.POST)
            #print (request.POST.get('codigo'))
            if foxr.is_valid() and form2.is_valid():
                post = foxr.save(commit=False)
                numero_nivel = 8
                post.is_active=1
                post2=form2.save(commit=False)

                lista_num =[1,2,3,4,5,6]
                if numero_nivel in lista_num:
                    post2.cod_area = unidad2.objects.get(pk=16)

                lista_coord = [2]
                if numero_nivel in lista_coord:
                    post.is_superuser=True
                post2.cod_area = unidad2.objects.get(pk=request.user.datos.cod_area.pk)
                post.save()
                post2.nivel_usua = NivelesNum.objects.get(pk=numero_nivel)
                usuario1 = User.objects.get(pk=post.pk)
                post2.usuario=usuario1
                
                post2.save()
                activate = True
                messages.success(request, 'Registro realizado exitosamente')
                return redirect('usuarioReport')
        else:
            foxr = UserCreationForm()
            form2 = Datos_per_infoF()
            form2 = None
            
            """
            for x in range(0,1):
                print (formlistoption[0].id)
            """
            #cambiado de form2 a form5 en el render
        return render(request, 'registros1_personal.html', {'form': foxr, "form5":form2, 'formOpti':formlistoption})
    return redirect('usuarioReport')


