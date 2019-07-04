from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser, Professor


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'fields': ('first_name', 'last_name', 'id_card', 'user_type'),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)


class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('docente','especialidades', 'state')
    list_editable = ('state',)
    date_hierarchy = 'created_at'
    readonly_fields = ('specialities', 'areas')
    list_filter = ('specialities__degree__name',)

    def especialidades(self, obj):
        return ",".join([e.degree.name for e in obj.specialities.all()]) #Hay que arreglar


    def docente(self, obj):
        return obj.user.get_full_name()


admin.site.register(Professor, ProfessorAdmin)