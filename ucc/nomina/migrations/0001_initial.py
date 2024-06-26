# Generated by Django 4.2 on 2024-02-24 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.IntegerField(unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=245)),
                ('tel', models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.IntegerField()),
                ('nombre_pro', models.CharField(max_length=254)),
                ('semestres', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EmpleadoPrograma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(choices=[('PRO', 'Profesor'), ('JEF', 'Jefes de Programa'), ('ADM', 'Administrativos')], default='PRO', max_length=20)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nomina.empleado')),
                ('programa', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='nomina.programa')),
            ],
        ),
    ]
