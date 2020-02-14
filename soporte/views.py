from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.utils import timezone

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse, FileResponse

from .models import unidad2 ,P_opci, sop_notif, P_detal, NivelDet, Datos
from django.contrib.auth.models import User

from .forms import CodigosF ,DatosRF ,P_detalF ,P_opciF,AuthenticationForm, sop_notifF, DatosF

from .Com import migracion

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
        form3Cod = CodigosF(request.POST)
        #print (request.POST.get('codigo'))
        if foxr.is_valid() and form2.is_valid():

            post = foxr.save(commit=False)
            post.is_active=0
            post2=form2.save(commit=False)
            post.save()
            usuario1 = User.objects.get(pk=post.pk)
            post2.usuario=usuario1
            post2.save()
            #Niveles.objects.create(user=User.objects.get(id=post.pk))
            
            return redirect('login')
    else:
        foxr = UserCreationForm()
        form2 = DatosRF()
        form3Cod = CodigosF()
        
        """
        for x in range(0,1):
            print (formlistoption[0].id)
        """
    return render(request, 'registros1.html', {'form3':form3Cod,'form': foxr, "form2":form2, 'formOpti':formlistoption})


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



def post_list(request):
    #print (request.user.niveles.Nivel)
    posts=None
    return redirect('login')
    return render(request, 'post_list.html', {'posts': posts})

def post_list2(request):
    #print (request.user.niveles.Nivel)
    posts=None
    if request.method == "POST":
        form = sop_notifF(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.cod_usu = request.user
            #post.fedicion = timezone.now()
            post.save()
            return redirect('post_noti')
    else:
        if (request.user.is_superuser or request.user.is_staff):
            form = None
        else:
            form = sop_notifF()
    return render(request, 'post_list2.html', {'posts': posts, 'form': form})



def a_us(request):
    if request.user.is_authenticated==True:
        
        v_us = User.objects.filter(is_active=0).order_by('id')
        Verthandi=[]
        for Skuld in v_us:
            try:
                datos = Datos.objects.get(pk=Skuld.pk)
                Verthandi.append(datos)
            except:
                pass

        return render(request, 'v_us2.html', {'v_us': v_us,'datos':Verthandi})
    
    else:
        return HttpResponseRedirect("/")



def userAP(request, pk):
    if request.user.is_superuser:
        Verthandi = get_object_or_404(User, pk=pk)
        #print (Verthandi['is_active'])
        Verthandi.is_active = False
        #Verthandi.is_active = True
        Verthandi.save()
        return redirect('a_us')

    else:
        return redirect ("/")


def userNE(request, pk):
    if request.user.is_superuser:
        Verthandi = get_object_or_404(User, pk=pk)
        Verthandi.delete()
        
        return redirect('a_us')

    else:
        return redirect ("/")


def datos_u(request, pk):
    try:
        dat=Datos.objects.get(pk=pk)
        Verthandi=User.objects.get(pk=pk)
            
        datos = get_object_or_404(Datos, pk=pk)
        return render(request, 'datos_u.html', {'datos': datos,'dat': dat,'usuario1':Verthandi})

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
    if request.user.is_superuser or request.user.is_superuser:
        pass
    else:
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


def notiFalla(request):
    return render(request, 'notiF_detalle.html')

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

    return render(request, 'valids.html', {'code': post})

def Valid1_codigo(request):
    if request.user.is_superuser or request.user.is_staff:
        if request.method == "POST":
            while True:
                x12 = random.randint(100000000000, 999999999999)
                if not Codigos.objects.filter(codigo=x12).exists() :
                    Codigos.objects.create(codigo=x12)
                    return redirect('Valid_v')


        else:
            form = ValidF()
        return render(request, 'valid.html', {'form': form})
    else:
        return redirect('Error1')

def Error(request):
    return render(request, "Negado.html")
