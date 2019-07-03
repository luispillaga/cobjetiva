from django.db import models


# Create your models here.
from django.utils.timezone import now


class Period(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=100)
    start_date = models.DateField(verbose_name="Fecha inicio", default=now)
    end_date = models.DateField(verbose_name="Fecha finalización", default=now)
    created_at = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Fecha de actualiación", auto_now=True)

    class Meta:
        verbose_name = "Periodo"
        verbose_name_plural = "Periodos"

    def __str__(self):
        return self.name


class Area(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=100)
    description = models.TextField(verbose_name="Descripción")
    created_at = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Fecha de actualiación", auto_now=True)

    class Meta:
        verbose_name = "Área"
        verbose_name_plural = "Areas"

    def __str__(self):
        return self.name


class Specialty(models.Model):
    LEVELS_TYPE = (
        ('third', 'Tercer Nivel'),
        ('fourth', 'Cuarto Nivel'),
    )
    number = models.CharField(verbose_name="Número de registro", max_length=20)
    degree = models.CharField(verbose_name="Título", max_length=10, choices=LEVELS_TYPE)
    type = models.CharField(verbose_name="Tipo", max_length=100)
    created_at = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Fecha de actualiación", auto_now=True)

    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"

    def __str__(self):
        return self.degree


class Course(models.Model):
    period = models.ForeignKey(Period, verbose_name="Periodo", on_delete=models.CASCADE)
    area = models.ForeignKey(Area, verbose_name="Área capacitación", on_delete=models.DO_NOTHING)
    specialty = models.ForeignKey(Specialty, verbose_name="Especialidad", on_delete=models.DO_NOTHING)
    name = models.CharField(verbose_name="Nombre capacitación", max_length=100)
    accredited_hours = models.IntegerField(verbose_name="Horas acreditadas", default=1)
    place = models.CharField(verbose_name="Lugar", max_length=50)
    start_date = models.DateField(verbose_name="Fecha inicio", default=now)
    end_date = models.DateField(verbose_name="Fecha finalización", default=now)
    created_at = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Fecha de actualiación", auto_now=True)

    class Meta:
        verbose_name = "Capacitación"
        verbose_name_plural = "Capacitaciones"

    def __str__(self):
        return self.name




# class Inscription(models.Model):
#     pass