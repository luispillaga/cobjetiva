from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now
from training.models import Specialty, Area


class CustomUser(AbstractUser):
    USER_TYPE = (
        ('A', 'Administrador'),
        ('D', 'Docente'),
        ('RH', 'Recursos Humanos'),
    )
    id_card = models.CharField(max_length=10, verbose_name="Cédula")
    user_type = models.CharField(max_length=2, verbose_name="Tipo de Usuario", choices=USER_TYPE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Professor(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, verbose_name="Usuario")
    specialities = models.ManyToManyField(Specialty, verbose_name="Especialidades")
    areas = models.ManyToManyField(Area, verbose_name="Areas de preferencia")
    phone = models.CharField(verbose_name="Teléfono", max_length=12)
    city = models.CharField(verbose_name="Ciudad", max_length=20)
    address = models.CharField(verbose_name="Dirección", max_length=50)
    birthday_date = models.DateField(verbose_name="Fecha de nacimiento", default=now)
    state = models.BooleanField(verbose_name="Activo", default=False)

    class Meta:
        verbose_name = "Docente"
        verbose_name_plural = "Docentes"

    def __str__(self):
        return self.user.first_name
