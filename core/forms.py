from django import forms
from django.contrib.auth import get_user_model

from training.models import Specialty
from users.models import Professor


class UserEditForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('id_card', 'first_name', 'last_name', 'email')
        widgets = {
            'id_card': forms.TextInput(attrs={'class': 'form-control form-control-alternative'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-alternative'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-alternative'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-alternative'}),
        }


class ProfessorEditForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ('phone', 'city', 'address', 'birthday_date')
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control form-control-alternative'}),
            'city': forms.TextInput(attrs={'class': 'form-control form-control-alternative'}),
            'address': forms.TextInput(attrs={'class': 'form-control form-control-alternative'}),
            'birthday_date': forms.DateInput(attrs={'class':'form-control form-control-alternative'}),
        }


class SpecialtyCreateForm(forms.ModelForm):
    class Meta:
        model = Specialty
        fields = ('degree', 'education_center', 'number', 'level_type', 'degree_type', 'emission_date')
        widgets = {
            'degree': forms.Select(attrs={'class':'form-control form-control-alternative'}),
            'education_center': forms.TextInput(attrs={'class':'form-control form-control-alternative'}),
            'number': forms.TextInput(attrs={'class':'form-control form-control-alternative'}),
            'level_type': forms.Select(attrs={'class':'form-control form-control-alternative'}),
            'degree_type': forms.Select(attrs={'class':'form-control form-control-alternative'}),
            'emission_date': forms.SelectDateWidget(attrs={'class':'form-control form-control-alternative'}),
        }

    def __init__(self, *args, **kwargs):
        super(SpecialtyCreateForm, self).__init__(*args, **kwargs)
        self.fields['degree'].empty_label = "Seleccione un título"
