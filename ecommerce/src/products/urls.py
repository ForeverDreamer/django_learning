from django.conf.urls import url

from .views import ProductListView, product_list_view

urlpatterns = [
    url(r'^$', ProductListView.as_view()),
    url(r'^fbc/$', product_list_view),
]
