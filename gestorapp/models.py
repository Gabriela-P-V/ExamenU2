from django.db import models

# Create your models here.
class Carrera(models.Model):
    ncarrera = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'Carrera {self.id}: {self.ncarrera}'

class Alumno(models.Model):
    nombrealumno = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    semestre = models.IntegerField()
    carrera = models.ForeignKey(Carrera ,on_delete=models.SET_NULL,null=True)


    def __str__(self) -> str:
        return f'Alumno {self.id}: {self.nombrealumno}, Apellido {self.apellido}, Semestre {self.semestre}, Carrera {self.carrera}'

class Maestro(models.Model):
    nombremaestro = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'Maestro {self.id}: {self.nombremaestro}'

class Materia(models.Model):
    nombremateria = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'Materia  {self.id}: {self.nombremateria}'

class MaestroMateria(models.Model):
    maestro = models.ForeignKey(Maestro,on_delete=models.SET_NULL,null=True)
    materia = models.ForeignKey(Materia,on_delete=models.SET_NULL,null=True)
    def __str__(self) -> str:
        return f'Horario {self.id}: Mestro {self.maestro}, Materia {self.materia}'