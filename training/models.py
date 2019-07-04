from django.db import models
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


class Degree(models.Model):
    name = models.CharField(verbose_name="Nombre especialidad", max_length=100)

    class Meta:
        verbose_name = "Título"
        verbose_name_plural = "Titulos"

    def __str__(self):
        return self.name


class Specialty(models.Model):
    LEVELS_TYPE = (
        ('third', 'Tercer Nivel'),
        ('fourth', 'Cuarto Nivel'),
    )
    DEGREE_TYPE = (
        ('na', 'Nacional'),
        ('in', 'Internacional'),
    )
    degree = models.ForeignKey(Degree, verbose_name="Título", on_delete=models.DO_NOTHING, null=True)
    education_center = models.CharField(verbose_name="Unidad educativa", max_length=100)
    number = models.CharField(verbose_name="Número de registro", max_length=20)
    level_type = models.CharField(verbose_name="Nivel", max_length=100, choices=LEVELS_TYPE)
    degree_type = models.CharField(verbose_name="Tipo de título", max_length=100, choices=DEGREE_TYPE)
    emission_date = models.DateField(verbose_name="Fecha de emisión", null=True, blank=True)
    created_at = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Fecha de actualiación", auto_now=True)

    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"

    def __str__(self):
        return self.degree.name


class Course(models.Model):
    COURSE_STATE = (
        ('inscriptions', 'Inscripciones'),
        ('emission', 'Emisión'),
        ('finished', 'Finalizado'),
    )
    period = models.ForeignKey(Period, verbose_name="Periodo", on_delete=models.CASCADE)
    area = models.ForeignKey(Area, verbose_name="Área capacitación", on_delete=models.DO_NOTHING, null=True)
    name = models.CharField(verbose_name="Nombre capacitación", max_length=100)
    accredited_hours = models.IntegerField(verbose_name="Horas acreditadas", default=1)
    place = models.CharField(verbose_name="Lugar", max_length=50)
    start_date = models.DateField(verbose_name="Fecha inicio", default=now)
    end_date = models.DateField(verbose_name="Fecha finalización", default=now)
    state = models.CharField(verbose_name="Estado capacitación", max_length=15, choices=COURSE_STATE, default='inscriptions')
    created_at = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Fecha de actualiación", auto_now=True)

    class Meta:
        verbose_name = "Capacitación"
        verbose_name_plural = "Capacitaciones"

    def __str__(self):
        return self.name


class Inscription(models.Model):
    professor = models.ForeignKey('users.Professor', verbose_name="Docente", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name="Capacitación", on_delete=models.CASCADE)
    inscription_at = models.DateTimeField(verbose_name="Fecha de inscripción", default=now)
    created_at = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Fecha de actualiación", auto_now=True)

    class Meta:
        verbose_name = "Inscripción"
        verbose_name_plural = "Inscripciones"

    def __str__(self):
        return "{} - {} {}".format(self.course.name,
                                   self.professor.user.first_name, self.professor.user.last_name)
