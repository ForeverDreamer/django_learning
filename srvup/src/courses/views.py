import random
from django.http import Http404

from django.views.generic import (
        ListView,
        CreateView,
        DetailView,
        UpdateView,
        DeleteView,
    )

from .models import Course
from .forms import CourseForm
from videos.mixins import MemberRequiredMixin, StaffMemberRequiredMixin


class CourseListView(ListView):
    def get_queryset(self):
        request = self.request
        qs = Course.objects.all()
        query = request.GET.get('q')
        if query:
            qs = qs.filter(title__icontains=query)
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(CourseListView, self).get_context_data(*args, **kwargs)
        context['random_number'] = random.randint(100, 10000)
        print(context)
        return context


class CourseCreateView(StaffMemberRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(CourseCreateView, self).form_valid(form)


class CourseDetailView(MemberRequiredMixin, DetailView):
    queryset = Course.objects.all()

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        # obj = Course.objects.get(slug=slug)  # 1 or 0; > 1 MultipleObjectsReturned
        qs = Course.objects.filter(slug=slug)
        if qs.exists():
            return qs.first()
        raise Http404
        # try:
        #     obj = Course.objects.get(slug=slug)
        # except Course.MultipleObjectsReturned:
        #     qs = Course.objects.filter(slug=slug)
        #     if qs.exists():
        #         obj = qs.first()
        # except:
        #     raise Http404
        # return obj


class CourseUpdateView(StaffMemberRequiredMixin, UpdateView):
    queryset = Course.objects.all()
    form_class = CourseForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        if not self.request.user.is_staff:
            obj.user = self.request.user
        obj.save()
        return super(CourseUpdateView, self).form_valid(form)

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        # obj = Course.objects.get(slug=slug)  # 1 or 0; > 1 MultipleObjectsReturned
        qs = Course.objects.filter(slug=slug)
        if qs.exists():
            return qs.first()
        raise Http404


class CourseDeleteView(StaffMemberRequiredMixin, DeleteView):
    queryset = Course.objects.all()
    success_url = '/videos/'



