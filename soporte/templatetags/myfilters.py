from django import template

register = template.Library()

@register.filter(name='addclass')
def addclass(value, arg):

    return value.as_widget(attrs={'class': arg})

"""
def addcss(value, arg):
    css_classes = value.field.widget.attrs.get('class', '').split(' ')
    if css_classes and arg not in css_classes:
        css_classes = '%s %s' % (css_classes, arg)
    return value.as_widget(attrs={'class': css_classes})
"""

@register.filter(name='addplaceh')
def addclass(value, arg):
    return value.as_widget(attrs={'placeholder': arg})


@register.filter(name='login1')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg,'placeholder': "Usuario"})
@register.filter(name='login2')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg,"placeholder": "Contraseña"})



@register.filter(name='notifa1')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg,'placeholder': "Nombre"})
@register.filter(name='notifa2')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg,"placeholder": "Numero Pc"})
@register.filter(name='notifa3')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg,"placeholder": "Detalles del problema"})



@register.filter(name='regist1')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg,"placeholder": "Usuario"})
@register.filter(name='regist2')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg,"placeholder": "Contraseña"})
@register.filter(name='regist3')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg,"placeholder": "Confirmar"})
@register.filter(name='regist4')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg,"placeholder": "Nombre"})
@register.filter(name='regist5')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg,"placeholder": "Apellido"})
@register.filter(name='regist6')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg,"placeholder": "Cedula"})

