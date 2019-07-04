from django.contrib import admin
from .models import Area, Specialty, Period, Course, Inscription, Degree


# Register your models here.
@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    pass
    # list_display = ('name',)


@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    pass


@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
    pass
