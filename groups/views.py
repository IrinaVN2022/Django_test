from students.models import Student
from .forms import CreateGroupForm, UpdateGroupForm
from .models import Group
from courses.models import Course
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class ListGroupView(ListView):
    model = Group  # object_list
    template_name = 'groups/list.html'


'''def get_render_create(request: HttpRequest):
    if request.method == 'GET':
        form = CreateGroupForm()
    elif request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(request=request,
                  template_name='groups/create.html',
                  context={'form': form})'''


class CreateGroupView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = CreateGroupForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/create.html'

    def form_valid(self, form):
        response = super().form_valid(form)

        new_group = form.save()

        students = form.cleaned_data['students']
        for student in students:
            student.group = new_group
            student.save()

        return response


'''def get_render_update(request: HttpRequest, pk: int):
    group = Group.objects.get(pk=pk)
    students = {'students': Student.objects.filter(group=group)}
    if request.method == 'GET':
        form = UpdateGroupForm(instance=group, initial=students)
    elif request.method == 'POST':
        form = UpdateGroupForm(data=request.POST, instance=group, initial=students)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(request=request,
                  template_name='groups/update.html',
                  context={'form': form})'''


class UpdateGroupView(LoginRequiredMixin, UpdateView):
    model = Group
    form_class = UpdateGroupForm
    success_url = reverse_lazy('groups:list')
    template_name = 'groups/update.html'

    def get_initial(self):
        initial = super().get_initial()
        try:

            initial['headman_field'] = self.object.headman.pk
        except AttributeError:
            pass

        return initial

    def form_valid(self, form):
        response = super().form_valid(form)

        students = form.cleaned_data['students']
        for student in students:
            student.group = self.object
            if hasattr(student, 'headman_group'):
                group = student.headman_group
                group.headman = None
                group.save()
            student.save()
        headman_pk = int(form.cleaned_data.get('headman_field'))
        if headman_pk:
            form.instance.headman = Student.objects.get(pk=headman_pk)
        else:
            form.instance.headman = None

        form.save()
        return response


'''def get_render_detail(request: HttpRequest, pk: int):
    group = Group.objects.get(pk=pk)
    return render(request=request,
                  template_name='groups/detail.html',
                  context={'group': group})'''


class DetailGroupView(LoginRequiredMixin, DetailView):
    model = Group
    template_name = 'groups/detail.html'


'''def get_render_delete(request: HttpRequest, pk: int):
    group = Group.objects.get(pk=pk)
    if request.method == 'POST':
        print('POST')
        group.delete()
        return HttpResponseRedirect(reverse('groups:list'))
    return render(request=request,
                  template_name='groups/delete.html',
                  context={'group': group})'''


class DeleteGroupView(LoginRequiredMixin, DeleteView):
    model = Group
    template_name = 'groups/delete.html'
    success_url = reverse_lazy('groups:list')
