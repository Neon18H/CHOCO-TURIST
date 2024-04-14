from django.db import models

# Create your models here.


class Empleado(models.Model):
    cedula = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(max_length=245, unique= True)
    password = models.CharField(max_length=254)
    tel =  models.CharField(max_length=15, null= True,)
    TIPOS=(
        (1,"Administrador"),
        (2,"Coordinador"),
        (3,"Profesor"),
    )

    tipo_usuario = models.IntegerField(choices=TIPOS,default=3)
    def __str__(self):
        return f"{self.nombre} {self.apellido} "


class Programa(models.Model):
    cod = models.IntegerField()
    nombre_pro= models.CharField(max_length=254)
    semestres = models.IntegerField()
    def __str__(self):
        return f"{self.nombre_pro} "

class EmpleadoPrograma(models.Model):
    empleado= models.ForeignKey(Empleado, on_delete=models.DO_NOTHING)
    programa= models.ForeignKey(Programa, on_delete=models.DO_NOTHING)
    ROLES =(
        ("PRO", "Profesor"),
        ("JEF" ,"Jefes de Programa"),
        ("ADM", "Administrativos"),
    )
    rol= models.CharField(max_length=20, choices=ROLES, default="PRO")
    def __str__(self):
        return f"{self.id} - {self.rol} - {self.programa}"
    
