from django.urls import path

from .views import (
    CourseListView,
    CourseCreateView,
    CourseDetailView,
    CourseUpdateView,
    CourseDeleteView,
    LectureDetailView,
)

urlpatterns = [
    path('', CourseListView.as_view(), name='list'),
    # 放在video-detail前面，注意url匹配顺序，否则会把create当slug匹配
    path('create/', CourseCreateView.as_view(), name='create'),
    path('<str:slug>/', CourseDetailView.as_view(), name='detail'),
    path('<str:slug>/edit/', CourseUpdateView.as_view(), name='update'),
    path('<str:slug>/delete/', CourseDeleteView.as_view(), name='delete'),
    path('<str:cslug>/<str:lslug>/', LectureDetailView.as_view(), name='lecture-detail'),
]
