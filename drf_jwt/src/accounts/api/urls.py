from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


from .views import AuthView

urlpatterns = [
    url(r'^$', AuthView.as_view()),
    url(r'^jwt/$', obtain_jwt_token),
    url(r'^jwt/refresh/$', refresh_jwt_token),
]
