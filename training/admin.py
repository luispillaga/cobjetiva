from django.contrib import admin
from .models import Area, Specialty, Period, Course


# Register your models here.
@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('degree',)


@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)
