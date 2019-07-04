from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from core.forms import UserEditForm, ProfessorEditForm, SpecialtyCreateForm
from training.models import Specialty


@login_required
def home(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        professor_form = ProfessorEditForm(
            instance=request.user.professor,
            data=request.POST,
            files=request.FILES
        )
        if user_form.is_valid() and professor_form.is_valid():
            user_form.save()
            professor_form.save()
            messages.success(request, 'Tus datos personales han sido modificados.')
    else:
        user_form = UserEditForm(instance=request.user)
        professor_form = ProfessorEditForm(
            instance=request.user.professor
        )
    return render(request, 'core/home.html',
                  {'user_form': user_form,
                   'professor_form': professor_form})


class SpecialtyList(ListView):
    model = Specialty
    template_name = 'specialty/specialty_list.html'
    context_object_name = 'specialties'

    def get_queryset(self):
        professor_list = [self.request.user.professor]
        return Specialty.objects.filter(professors__in=professor_list)


class SpecialtyCreate(CreateView):
    model = Specialty
    template_name = "specialty/specialty_form.html"
    form_class = SpecialtyCreateForm
    success_url = reverse_lazy('specialty_list')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = self.get_object

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            specialty = form.save()
            professor = request.user.professor
            professor.specialities.add(specialty)
            professor.save()
            return HttpResponseRedirect(self.get_success_url())


class SpecialtyUpdate(UpdateView):
    model = Specialty
    form_class = SpecialtyCreateForm
    template_name = "specialty/specialty_form.html"
    success_url = reverse_lazy('specialty_list')


def specialty_delete(request, id):
    specialty = get_object_or_404(Specialty, pk=id)
    specialty.delete()
    messages.success(request, 'La especialidad ha sido eliminada.')
    return redirect('specialty_list')
