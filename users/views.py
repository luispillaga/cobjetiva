from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from users.forms import LoginForm, UserRegistrationForm, UserEditForm
from users.models import Professor


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
                    return HttpResponse('Autenticado')
                else:
                    return HttpResponse('Aún no esta habilitado para usar el sistema')
            else:
                return HttpResponse('Invalid login')
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


@login_required
def edit(request):
    # if request.method == 'POST':
    #     user_form = UserEditForm(instance=request.user,
    #                              data=request.POST)
    #     company_form = CompanyEditForm(
    #         instance=request.user.company,
    #         data=request.POST,
    #         files=request.FILES
    #     )
    #     if user_form.is_valid() and company_form.is_valid():
    #         user_form.save()
    #         company_form.save()
    # else:
    #     user_form = UserEditForm(instance=request.user)
    #     company_form = CompanyEditForm(
    #         instance=request.user.company
    #     )
    return render(request, 'account/edit.html')
