from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from users.models import CustomUser, Professor


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# Formularios para registro
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Contraseña", required=True, widget=forms.PasswordInput(
        attrs={'class':'input100'}
    ))
    password2 = forms.CharField(label="Contraseña", required=True, widget=forms.PasswordInput(
        attrs={'class':'input100'}
    ))

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return cd['password2']

