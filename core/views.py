from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from core.forms import UserEditForm, ProfessorEditForm, SpecialtyCreateForm, AreaCreateForm, AreaForm
from training.models import Specialty, Area, Inscription


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
    template_name = 'core/specialty/specialty_list.html'
    context_object_name = 'specialties'

    def get_queryset(self):
        professor_list = [self.request.user.professor]
        return Specialty.objects.filter(professors__in=professor_list)


class SpecialtyCreate(CreateView):
    model = Specialty
    template_name = "core/specialty/specialty_form.html"
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
    template_name = "core/specialty/specialty_form.html"
    success_url = reverse_lazy('specialty_list')


def specialty_delete(request, id):
    specialty = get_object_or_404(Specialty, pk=id)
    specialty.delete()
    messages.success(request, 'La especialidad ha sido eliminada.')
    return redirect('specialty_list')


# Controladores de Areas
class AreaList(ListView):
    model = Area
    template_name = 'core/area/area_list.html'
    context_object_name = 'areas'

    def get_queryset(self):
        professor_list = [self.request.user.professor]
        return Area.objects.filter(professors__in=professor_list)


def area_assigment(request):
    if request.method == 'POST':
        form = AreaForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            area = cd['area']
            professor = request.user.professor
            professor.areas.add(area)
            professor.save()
            return redirect('/myareas/')

    else:
        form = AreaForm()
    return render(request, 'core/area/area_assigment.html', {'form': form})


def get_description(request):
    try:
        id = request.GET.get('id', None)
        area = Area.objects.get(pk=id)
        description = area.description
        data = {
            'description': description
        }
    except Exception:
        data = {
            'description': ""
        }
    return JsonResponse(data)


class AreaCreate(CreateView):
    model = Area
    template_name = "core/area/area_form.html"
    form_class = AreaCreateForm
    success_url = reverse_lazy('area_list')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = self.get_object

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            area = form.save()
            professor = request.user.professor
            professor.areas.add(area)
            professor.save()
            return HttpResponseRedirect(self.get_success_url())


class AreaUpdate(UpdateView):
    model = Area
    form_class = AreaCreateForm
    template_name = "core/area/area_form.html"
    success_url = reverse_lazy('area_list')


def area_delete(request, id):
    professor = request.user.professor
    area = get_object_or_404(Area, pk=id)
    professor.areas.remove(area)
    messages.success(request, 'El área ha sido eliminada.')
    return redirect('area_list')


# Controladores de Inscripción
class InscriptionList(ListView):
    model = Inscription
    template_name = 'core/inscription/inscription_list.html'
    context_object_name = 'inscriptions'

    def get_queryset(self):
        professor = self.request.user.professor
        inscriptions = Inscription.objects.filter(professor=professor)
        return inscriptions
