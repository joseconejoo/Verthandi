from django import forms
import pdb
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm as AuthForm
from django.contrib.auth import (
    authenticate, get_user_model, password_validation, backends
)
from django.utils.translation import gettext as _
UserModel = get_user_model()

from .models import permisos_emple, sop_notif_mes, bie_gob_bienes, report_usu_area, NivelesNum, Codigos, unidad2, P_opci ,Datos, NivelDet, sop_notif, P_detal

from .Fun1 import usu_1xnivel_sub_area2Form


class perm_emple_nuevo(forms.ModelForm):
	cedula = forms.IntegerField(
	    label=_("cedula"),
	)

	class Meta:
		model = permisos_emple
		fields = ('fecha_ini_per','fecha_fin_per')
	field_order = ['cedula','fecha_ini_per','fecha_fin_per']
	"""
	def __init__(self, *args, **kwargs):
	    super().__init__(*args, **kwargs)
	    #pdb.set_trace()
	    if self.data.get('cedula'):
	    	pdb.set_trace()
	    	cedu = self.data.get('cedula')
	    	if not (User.objects.filter(datos__cedula=cedu).exists()):
	    		raise self.codigo_e_invalid()
	    	cedu2p = User.objects.get(datos__cedula=cedu)
	    	cedu = cedu2p.pk
	    	_mutable = self.data._mutable
	    	self.data._mutable = True
	    	self.data['cod_area'] = cedu
	    	self.data._mutable = _mutable
	"""


class actu_contra(forms.ModelForm):
	password1 = forms.CharField(
	    label=_("Password"),
	    strip=False,
	    widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
	    help_text=password_validation.password_validators_help_text_html(),
	)
	password2 = forms.CharField(
	    label=_("Password confirmation"),
	    widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
	    strip=False,
	    help_text=_("Enter the same password as before, for verification."),
	)

	class Meta:
	    model = User
	    fields = ()

	def clean(self):
		password = self.cleaned_data.get('password2')
		if password:
		    try:
		        password_validation.validate_password(password, self.instance)
		    except forms.ValidationError as error:
		        self.add_error('password2', error)



class recu_contra(forms.ModelForm):
	error_messages = {
	    'No_existe': _("El usuario \"%(usuario)s\" no existe."),
	}
	def codigo_e_invalid(self):

	    return forms.ValidationError(
	        self.error_messages['No_existe'],
	        code='Codigo12',
	        params={'usuario': self.data.get('username')},
	    )

	class Meta:
	    model = User
	    fields = ("username",)
	def clean(self):
		usuario_a = self.data.get('username')
		if not (User.objects.filter(username=usuario_a).exists()):
			raise self.codigo_e_invalid()


class sop_notif_mesF(forms.ModelForm):
	class Meta:
		model = sop_notif_mes
		fields = ('mensaje','tipo_sop','estado_sop')

class CodigosF(forms.ModelForm):
	class Meta:
		model = Codigos
		fields = ('codigo',)

class P_detalF(forms.ModelForm):
	class Meta:
		model = P_detal
		fields = ('nombre',)

class P_opciF(forms.ModelForm):
	class Meta:
		model = P_opci
		fields = ('nombre',)

class report_usu_areaF(forms.ModelForm):
	class Meta:
		model = report_usu_area
		fields = ('cod_area',)
class Datos_per_infoF(forms.ModelForm):
	class Meta:
		model = Datos
		fields = ('nombre', 'apellido','cedula','sub_area')

class DatosF(forms.ModelForm):
	class Meta:
		model = Datos
		fields = ('nombre', 'apellido')

class DatosRF(forms.ModelForm):
	class Meta:
		model = Datos
		fields = ('nombre', 'apellido','cedula','cod_area','nivel_usua','sub_area')

	def __init__(self, *args, **kwargs):
	    super().__init__(*args, **kwargs)
	    #pdb.set_trace()
	    if self.data.get('cod_area'):
	    	cod_area2 = self.data.get('cod_area')
	    	cod_area2p = unidad2.objects.get(nom_unidad__exact=cod_area2)
	    	cod_area2 = cod_area2p.pk
	    	_mutable = self.data._mutable
	    	self.data._mutable = True
	    	self.data['cod_area'] = cod_area2
	    	self.data._mutable = _mutable
	    self.fields['nivel_usua'].queryset = NivelesNum.objects.none()
	    #self.fields['sub_area'].queryset = P_opci.objects.none()

	    if 'cod_area' in self.data:
	        try:
	            niveles_id = int(self.data.get('cod_area'))

	            self.fields['nivel_usua'].queryset = NivelesNum.objects.filter().order_by('id')
	            if niveles_id == 16:
	            	pass
	        except (ValueError, TypeError):
	            pass  # invalid input from the client; ignore and fallback to empty City queryset
	    elif self.instance.pk:
	        self.fields['nivel_usua'].queryset = self.instance.cod_area.Niveles_Num_set.order_by('name')




class sop_notifF(forms.ModelForm):
	error_messages = {
	    'Codigo12': _("El codigo \"%(codigo)s\" de equipo es invalido."),
	}
	def codigo_e_invalid(self):

	    return forms.ValidationError(
	        self.error_messages['Codigo12'],
	        code='Codigo12',
	        params={'codigo': self.data.get('num_pc')},
	    )
	class Meta:
		model = sop_notif
		#fields = ('tipo_sop','descrip1','problemaAd','nombre','num_pc')
		fields = ('problemaAd','nombre','num_pc')

	def __init__(self, *args, **kwargs):
	    super().__init__(*args, **kwargs)
	    """
	    self.dat = self.data.get('num_pc')
	    if not(bie_gob_bienes.objects.filter(codigo_e=self.dat).exists()) and not(self.dat == None):
	    	raise self.codigo_e_invalid()
	    """
	    """
	    self.fields['descrip1'].queryset = P_detal.objects.none()

	    if 'tipo_sop' in self.data:
	        try:
	            tipo_sop_id = int(self.data.get('tipo_sop'))
	            self.fields['descrip1'].queryset = P_detal.objects.filter(p_opci_id=tipo_sop_id).order_by('nombre')
	        except (ValueError, TypeError):
	            pass 
	    elif self.instance.pk:
	        self.fields['descrip1'].queryset = self.instance.tipo_sop.P_detal_set.order_by('nombre')
		"""
	def clean(self):
		cleaned_data = super().clean()
		numero_e = cleaned_data.get("num_pc")
		#print (numero_e)
		#print (bie_gob_bienes.objects.get(codigo_e__exact=str(numero_e)))
		if not(bie_gob_bienes.objects.filter(codigo_e=str(numero_e)).exists()) and (numero_e!=None):
			raise self.codigo_e_invalid()



class ModelBackend2(backends.ModelBackend):
	def authenticate(self, request, username=None, password=None, **kwargs):
	    if username is None:
	        username = kwargs.get(UserModel.USERNAME_FIELD)
	    try:
	        user = UserModel._default_manager.get_by_natural_key(username)
	    except UserModel.DoesNotExist:
	        UserModel().set_password(password)
	    else:
	        if user.check_password(password):
	            return user



class AuthenticationForm(AuthForm):
	error_messages = {
	    'invalid_login': _(
	        "Please enter a correct %(username)s and password. Note that both "
	        "fields may be case-sensitive."
	    ),
	    'inactive': _("This account is inactive."),
	    'inactivo': _("Esta cuenta no esta activa."),
	}

	def clean(self):
	    username = self.cleaned_data.get('username')
	    password = self.cleaned_data.get('password')

	    if username is not None and password:
	        self.user_cache = authenticate(self.request, username=username, password=password)
	        self.auth = ModelBackend2()
	        self.authUser = False
	        
	        try:
	        	self.authUser = self.auth.authenticate(self.request, username=username,password=password)
	        except:
	        	pass
	        if self.authUser:
	        	if not self.authUser.is_active:
	        		raise self.get_inactive_user()
	        	else:
	        		self.validacion(self.user_cache)
        	else:
        		self.validacion(self.user_cache)
	    return self.cleaned_data

	def confirm_login_allowed(self, user):
	    if not user.is_active:
	        raise forms.ValidationError(
	            self.error_messages['inactive'],
	            code='inactive',
	        )

	def get_user(self):
	    return self.user_cache

	def get_invalid_login_error(self):

	    return forms.ValidationError(
	        self.error_messages['invalid_login'],
	        code='invalid_login',
	        params={'username': self.username_field.verbose_name},
	    )
	def get_inactive_user(self):

	    return forms.ValidationError(
	        self.error_messages['inactivo'],
	        code='inactivo',
	        params={'username': self.username_field.verbose_name},
	    )
	def validacion(self,user_cache):
		self.user_cache = user_cache
		if self.user_cache is None:
			raise self.get_invalid_login_error()

		else:
			self.confirm_login_allowed(self.user_cache)


