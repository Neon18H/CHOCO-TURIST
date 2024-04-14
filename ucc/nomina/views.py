from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
# Create your views here.

def index (request):
    auth = request.session.get("auth", False)
    if auth:
        return render(request, "index.html")
    else:
        return redirect("login_form")


def ver_empleados(request):
    return render(request,"empleados.html")


def ver_programas(request):
    return render(request,"programas.html")

def programa_detalle(request, id_programa):
    nombre=""
    if id_programa ==1:
        nombre="Software"
    elif id_programa ==2:
        nombre="Mecanica"
    elif id_programa ==3:
        nombre="Civil"
    else:
        nombre ="Error 404: Programa no existe"

    print(id_programa)
    context = {"programa": nombre}
    return render(request,"programa_detalle.html", context)

def formulario1(request):
    return render(request,"formularios/formulario1.html")

def procesar_f1(request):
    num1 = int(request.POST.get("num1"))
    num2 = int(request.POST.get("num2"))
    res = num1 + num2
    return HttpResponse(res)

def login_form(request):
    return render(request,"login/login.html")
 
def login(request):
    user = int(request.POST.get("cedula"))
    passw = request.POST.get("password")
    try:
        consulta = Empleado.objects.get(cedula= user, password= passw)
        request.session["auth"]= {
            "nombre": f"{consulta.nombre} {consulta.apellido}",
            "cedula": consulta.cedula,
            "tipo_usuario": consulta.tipo_usuario,
        }
        return redirect('index')
    
    except Empleado.DoesNotExist:
        request.session["auth"]= False
        return HttpResponse(f"Usiario incorrecto...")

def logout(request):
    del request.session["auth"]
    return redirect('login_form')