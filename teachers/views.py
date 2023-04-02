from django.middleware.csrf import get_token
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from .models import Teacher
from .forms import CreateTeacherForm
from .forms import UpdateTeacherForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

'''def get_render_list(request: HttpRequest):
    teachers = Teacher.objects.all().order_by('first_name')
    return render(request=request,
                  template_name='teachers/list.html',
                  context={'teachers': teachers})'''


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers/list.html'


'''def get_render_create(request: HttpRequest):
    if request.method == 'GET':
        form = CreateTeacherForm()
    elif request.method == 'POST':
        form = CreateTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))

    return render(request=request,
                  template_name='teachers/create.html',
                  context={'form': form})'''


class TeacherCreateView(CreateView):
    model = Teacher
    form_class = CreateTeacherForm
    template_name = 'teachers/create.html'
    success_url = reverse_lazy('teachers:list')


'''def get_render_update(request: HttpRequest, pk: int):
    teacher = Teacher.objects.get(pk=pk)
    if request.method == 'GET':
        form = UpdateTeacherForm(instance=teacher)
    elif request.method == 'POST':
        form = UpdateTeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))

    return render(request=request,
                  template_name='teachers/update.html',
                  context={'form': form})'''


class TeacherUpdateView(UpdateView):
    model = Teacher
    form_class = UpdateTeacherForm
    template_name = 'teachers/create.html'
    success_url = reverse_lazy('update:list')


'''def get_render_detail(request: HttpRequest, pk: int):
    teacher = Teacher.objects.get(pk=pk)
    return render(request=request,
                  template_name='teachers/detail.html',
                  context={'teacher': teacher})'''


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teachers/detail.html'


'''def get_render_delete(request: HttpRequest, pk: int):
    teacher = Teacher.objects.get(pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('teachers:list'))
    return render(request=request,
                  template_name='teachers/delete.html',
                  context={'teacher': teacher})'''


class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'teachers/delete.html'
    success_url = reverse_lazy('teachers:list')
