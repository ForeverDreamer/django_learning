from django.urls import path

from .views import VideoListView, VideoDetailView

urlpatterns = [
    path('', VideoListView.as_view(), name='video-list'),
    # path('<str:pk>/', VideoDetailView.as_view(), name='video-detail'),
    path('<str:slug>/', VideoDetailView.as_view(), name='video-detail'),
]
