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
            'fields': ('id_card', 'user_type'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)


class ProfessorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Professor, ProfessorAdmin)