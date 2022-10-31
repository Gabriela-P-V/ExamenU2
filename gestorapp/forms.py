
from tkinter import Widget
from django.forms import ModelForm
from .models import Carrera, Alumno, Materia, MaestroMateria, Maestro
from django import forms
from django.contrib.admin import widgets

class AlumnoForm(ModelForm):
    #meta datos = datos de los datos, se tiene un dato string, pero se tiene la max longitud, la cantidad de caracteres permitidos.
    class Meta:
        model = Alumno
        fields = '__all__'

class CarreraForm(ModelForm):
    #meta datos = datos de los datos, se tiene un dato string, pero se tiene la max longitud, la cantidad de caracteres permitidos.
    class Meta:
        model = Carrera
        fields = '__all__'

class MateriaForm(ModelForm):
    #meta datos = datos de los datos, se tiene un dato string, pero se tiene la max longitud, la cantidad de caracteres permitidos.
    class Meta:
        model = Materia
        fields = '__all__'

class MaestroForm(ModelForm):
    #meta datos = datos de los datos, se tiene un dato string, pero se tiene la max longitud, la cantidad de caracteres permitidos.
    class Meta:
        model = Maestro
        fields = '__all__'

class MaestroMateriaForm(ModelForm):
    #meta datos = datos de los datos, se tiene un dato string, pero se tiene la max longitud, la cantidad de caracteres permitidos.
    class Meta:
        model = MaestroMateria
        fields = '__all__'