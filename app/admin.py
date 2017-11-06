from django import forms
from django.contrib import admin
from .models import *


# Register your models here.
class MarcacioneAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'usuario',
        'fecha',
        'hora',
        'observaciones',
		'estado',
		'zona',
    )
    search_fields = ('usuario', 'fecha', 'hora','observaciones',)
    list_filter = ('fecha','usuario',)
    ordering = ('usuario','-fecha',)
	
class PerfileAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'usuario',
        'jefe',
    )
    ordering = ('usuario',)
	
class UsuarioAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'usuario',
    )
    ordering = ('usuario',)
	
class JefeSupermercadoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'usuario',
        'nombres',
        'apellidos',
    )
    ordering = ('usuario',)

class ContratoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'limite_usuarios',
        'fecha_caducidad',
        'creado',
        'modificado',
    )		
def _register(model, admin_class):
    admin.site.register(model, admin_class)
	
	
_register(Marcacione,MarcacioneAdmin)
_register(Perfile,PerfileAdmin)
_register(Usuario,UsuarioAdmin)
_register(JefeSupermercado,JefeSupermercadoAdmin)
_register(Contrato ,ContratoAdmin)
