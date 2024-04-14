from django.urls import path
from . import views

urlpatterns = [
    path("inicio/", views.index, name="index"),
    path("ver_empleados/", views.ver_empleados, name="ver_empleados"),
    path("ver_programas/", views.ver_programas, name="ver_programas"),
    path("programa_detalle/<int:id_programa>/", views.programa_detalle, name="programa_detalle"),
    path("formulario1/", views.formulario1, name="formulario1"),
    path("procesar_f1", views.procesar_f1, name="procesar_f1"),
    path("", views.login_form, name="login_form"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),

]

#Django
#MVT(Model, View, Template)