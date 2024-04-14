from django.contrib import admin
from .models import Empleado, Programa, EmpleadoPrograma
# Register your models here.
#admin.site.register(Empleado)
#admin.site.register(Programa)
#admin.site.register(EmpleadoPrograma)

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display =['cedula', 'nombre', 'apellido', 'correo', 'tel', 'tipo_usuario', 'password']
    search_fields =['cedula','nombre']


@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display =['cod', 'nombre_pro', 'semestres', ]
    search_fields =['semestre','nombre_pro']

@admin.register(EmpleadoPrograma)
class EmpleadoProgramaAdmin(admin.ModelAdmin):
    list_display =[ 'empleado', 'programa', 'rol', ]
    list_filter=['empleado', 'programa',]
    list_editable=['rol', 'programa',]
