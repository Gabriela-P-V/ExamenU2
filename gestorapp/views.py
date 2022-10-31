from gestorapp.forms import AlumnoForm,CarreraForm
from django.shortcuts import render,get_object_or_404, redirect
from .models import Carrera, Alumno, Materia, MaestroMateria, Maestro

# Create your views here
def agregaralumno(request):
        if request.method=="POST":
                formaAlumno = AlumnoForm(request.POST)
                if formaAlumno.is_valid():
                        formaAlumno.save()
                        return redirect('/confirmacion')
        else:
                formaCiudad = AlumnoForm()
                return render(request, 'agregaralumno.html', {'formaAlumno':formaAlumno})


def agregarcarrera(request):
        if request.method=="POST":
                formaCarrera = CarreraForm(request.POST)
                if formaCarrera.is_valid():
                        formaCarrera.save()
                        return redirect('')
        else:
                formaCarrera = CarreraForm()
                return render(request, 'agregarcarrera.html', {'formaCarrera':formaCarrera})
