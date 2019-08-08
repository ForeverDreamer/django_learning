from django.conf.urls import url

from .views import (
    ProductListView,
    product_list_view,
    ProductDetailView,
    product_detail_view
)

urlpatterns = [
    url(r'^$', ProductListView.as_view()),
    url(r'^fbc/$', product_list_view),
    url(r'^(?P<pk>\d+)$', ProductDetailView.as_view()),
    url(r'^fbc/(?P<pk>\d+)$', product_detail_view),
]
