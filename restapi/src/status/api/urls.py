from django.conf.urls import url

from .views import (
    # StatusListSearchAPIView,
    StatusAPIView,
    StatusCreateAPIView,
)


urlpatterns = [
    # url(r'^$', StatusListSearchAPIView.as_view()),
    url(r'^$', StatusAPIView.as_view()),
    url(r'create/$', StatusCreateAPIView.as_view()),
    # url(r'^(?P<id>\d+)/$', StatusAPIDetailView.as_view()),
    # url(r'^(?P<id>\d+)/update/$', StatusAPIDetailView.as_view()),
    # url(r'^(?P<id>\d+)/delete/$', StatusAPIDetailView.as_view()),
]


# Start with
# /api/status/ -> List
# /api/status/create -> Create
# /api/status/12/ -> Retrieve(Detail)
# /api/status/12/update -> Update
# /api/status/12/delete -> Delete

# End With
# /api/status/ -> List -> CRUD
# /api/status/1/ -> Detail -> CRUD

# Final
# /api/status/ -> CRUD & List & Search
