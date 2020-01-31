from django import forms
import pdb
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm as AuthForm
from django.contrib.auth import (
    authenticate, get_user_model, password_validation, backends
)
from django.utils.translation import gettext as _
UserModel = get_user_model()

from .models import unidad2, P_opci ,Datos, Niveles, sop_notif, P_detal

class P_detalF(forms.ModelForm):
	class Meta:
		model = P_detal
		fields = ('nombre',)

class P_opciF(forms.ModelForm):
	class Meta:
		model = P_opci
		fields = ('nombre',)

class DatosF(forms.ModelForm):
	class Meta:
		model = Datos
		fields = ('nombre', 'apellido','cedula')


class DatosRF(forms.ModelForm):
	class Meta:
		model = Datos
		fields = ('nombre', 'apellido','cod_area','cedula')

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



class NivelesF(forms.ModelForm):
	class Meta:
		model = Niveles
		fields = ('Nivel',)

class sop_notifF(forms.ModelForm):
	class Meta:
		model = sop_notif
		fields = ('tipo_sop','descrip1','problemaAd','nombre','num_pc')

	def __init__(self, *args, **kwargs):
	    super().__init__(*args, **kwargs)
	    self.fields['descrip1'].queryset = P_detal.objects.none()

	    if 'tipo_sop' in self.data:
	        try:
	            tipo_sop_id = int(self.data.get('tipo_sop'))
	            self.fields['descrip1'].queryset = P_detal.objects.filter(p_opci_id=tipo_sop_id).order_by('nombre')
	        except (ValueError, TypeError):
	            pass 
	    elif self.instance.pk:
	        self.fields['descrip1'].queryset = self.instance.tipo_sop.P_detal_set.order_by('nombre')





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
	    'inactivo': ("Esta cuenta no esta activa."),
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


