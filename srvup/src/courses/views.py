import random
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404

from django.views.generic import (
        ListView,
        CreateView,
        DetailView,
        UpdateView,
        DeleteView,
    )

from .models import Course, Lecture
from videos.mixins import MemberRequiredMixin, StaffMemberRequiredMixin
from .forms import CourseForm


class LectureDetailView(MemberRequiredMixin, DetailView):
    def get_object(self, queryset=None):
        course_slug = self.kwargs.get('cslug')
        lecture_slug = self.kwargs.get('lslug')
        # 实现方式1
        obj = get_object_or_404(Lecture, course__slug=course_slug, slug=lecture_slug)
        # 实现方式2
        # course_obj = Course.objects.get(slug=course_slug)
        # obj = Lecture.objects.get(course=course_obj, slug=lecture_slug)
        # 实现方式3
        # obj = Lecture.objects.filter(course__slug=course_slug, slug=lecture_slug).first()
        return obj


class CourseListView(ListView):
    def get_queryset(self):
        request = self.request
        qs = Course.objects.all()
        query = request.GET.get('q')
        user = self.request.user
        if query:
            qs = qs.filter(title__icontains=query)
        if user.is_authenticated:
            qs = qs.owned(user)
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
        qs = Course.objects.filter(slug=slug).owned(self.request.user)
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
