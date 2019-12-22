from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm as AuthForm
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
from django.utils.translation import gettext, gettext_lazy as _
UserModel = get_user_model()

from .models import Datos, Niveles, sop_notif, P_detal




class DatosF(forms.ModelForm):
	class Meta:
		model = Datos
		fields = ('nombre', 'apellido', 'cedula')

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


class AuthenticationForm(AuthForm):
	error_messages = {
	    'invalid_login': _(
	        "Please enter a correct %(username)s and password. Note that both "
	        "fields may be case-sensitive."
	    ),
	    'inactive': _("This account is inactive."),
	    'inactivo': ("Esta cuenta no ha sido aprobada."),
	}


	def clean(self):
	    username = self.cleaned_data.get('username')
	    password = self.cleaned_data.get('password')

	    if username is not None and password:
	        self.user_cache = authenticate(self.request, username=username, password=password)
	        self.verif = None
	        try:
	        	self.verif = User.objects.get(username=username)
	        except:
	        	pass

	        if self.verif:
	        	if not self.verif.is_active:
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
