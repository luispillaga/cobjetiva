from django.contrib import admin
from .models import Area, Specialty, Period, Course, Inscription, Degree


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('name','description')


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('name','education_center','level_type','degree_type','emission_date')
    date_hierarchy = 'emission_date'

    def name(self, obj):
        return obj.degree.name


@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('name','start_date','end_date')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'area', 'accredited_hours','place','start_date','end_date')
    search_fields = ('name',)
    date_hierarchy = 'start_date'


def area(self, obj):
        return obj.area.name


@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    pass
    #list_display=('profesor','course','cours_state')


@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
    pass
