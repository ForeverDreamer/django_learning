from django.conf.urls import url

from .views import game_detail


urlpatterns = [
    url(r'detail/(?P<game_id>\d+)/$',
        game_detail,
        name="gameplay_detail"),
]
