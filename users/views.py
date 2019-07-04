from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.forms import LoginForm, UserRegistrationForm
from users.models import Professor
from django.contrib import messages


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.professor.state:
                    login(request, user)
                    if 'next' in request.POST:
                        print(request.POST.get("next"))
                        return redirect(request.POST.get("next"))
                    return redirect('home')
                else:
                    message = 'Aún no se encuentra habilitado para iniciar sesión.'
                    return render(request, 'users/invalid_login.html', {'message': message})
            else:
                messages.error(request, 'Credenciales incorrectos.')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            Professor.objects.create(user=new_user)
            return render(request, 'users/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'users/register.html',
                  {'user_form': user_form})

