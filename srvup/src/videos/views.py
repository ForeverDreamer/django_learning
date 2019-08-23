import random

from django.views.generic import (
        ListView,
        CreateView,
        DetailView,
        UpdateView,
        DeleteView,
    )

from .models import Video
from .forms import VideoForm
from .mixins import MemberRequiredMixin, StaffMemberRequiredMixin


class VideoListView(ListView):
    def get_queryset(self):
        request = self.request
        qs = Video.objects.all()
        query = request.GET.get('q')
        if query:
            qs = qs.filter(title__icontains=query)
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(VideoListView, self).get_context_data(*args, **kwargs)
        context['random_number'] = random.randint(100, 10000)
        print(context)
        return context


class VideoCreateView(StaffMemberRequiredMixin, CreateView):
    model = Video
    form_class = VideoForm
    # success_url = '/success/'


class VideoDetailView(MemberRequiredMixin, DetailView):
    queryset = Video.objects.all()


class VideoUpdateView(StaffMemberRequiredMixin, UpdateView):
    queryset = Video.objects.all()
    form_class = VideoForm


class VideoDeleteView(StaffMemberRequiredMixin, DeleteView):
    queryset = Video.objects.all()
    success_url = '/videos/'



