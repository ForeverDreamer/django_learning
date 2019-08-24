from django.urls import path

from .views import (
    VideoListView,
    VideoDetailView,
    VideoCreateView,
    VideoUpdateView,
    VideoDeleteView
)

urlpatterns = [
    path('', VideoListView.as_view(), name='list'),
    # 放在video-detail前面，注意url匹配顺序，否则会把create当slug匹配
    path('create/', VideoCreateView.as_view(), name='create'),
    # path('<str:pk>/', VideoDetailView.as_view(), name='video-detail'),
    path('<str:slug>/', VideoDetailView.as_view(), name='detail'),
    path('<str:slug>/edit/', VideoUpdateView.as_view(), name='update'),
    path('<str:slug>/delete/', VideoDeleteView.as_view(), name='delete'),
]
