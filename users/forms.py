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


# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)
#
#
# # Formularios para registro
# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(label="Contraseña", required=True, widget=forms.PasswordInput(
#         attrs={'class':'input100'}
#     ))
#     password2 = forms.CharField(label="Contraseña", required=True, widget=forms.PasswordInput(
#         attrs={'class':'input100'}
#     ))
#
#     class Meta:
#         model = get_user_model()
#         fields = ('username', 'first_name', 'last_name', 'email')
#
#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password'] != cd['password2']:
#             raise forms.ValidationError('Las contraseñas no coinciden.')
#         return cd['password2']
#
#
# class UserEditForm(forms.ModelForm):
#     class Meta:
#         model = get_user_model()
#         fields = ('first_name', 'last_name', 'email')
#         widgets = {
#             'first_name': forms.TextInput(attrs={'class': 'form-control form-control-alternative'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control form-control-alternative'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control form-control-alternative'}),
#         }


# class CompanyEditForm(forms.ModelForm):
#     class Meta:
#         model = Professor
#         fields = ('name', 'address', 'phone', 'city', 'logo')
#         widgets = {
#             'name': forms.TextInput(attrs={'class':'form-control form-control-alternative'}),
#             'address': forms.TextInput(attrs={'class':'form-control form-control-alternative'}),
#             'phone': forms.TextInput(attrs={'class':'form-control form-control-alternative'}),
#             'city': forms.TextInput(attrs={'class':'form-control form-control-alternative'}),
#             'logo': forms.FileInput(attrs={'class':'form-control form-control-alternative'}),
#         }
