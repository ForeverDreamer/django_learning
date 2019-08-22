from django.shortcuts import render
from django.views.generic import (
        ListView,
        CreateView,
        DetailView,
        UpdateView,
        DeleteView,
    )

from .models import Video


class VideoListView(ListView):
    queryset = Video.objects.all()


class VideoCreateView(CreateView):
    queryset = Video.objects.all()


class VideoDetailView(DetailView):
    queryset = Video.objects.all()


class VideoUpdateView(UpdateView):
    queryset = Video.objects.all()


class VideoDeleteView(DeleteView):
    queryset = Video.objects.all()



