from django.conf.urls import url

from .views import (
    ProductListView,
    product_list_view,
    ProductDetailView,
    product_detail_view,
    ProductFeaturedListView,
    ProductFeaturedDetailView
)

urlpatterns = [
    url(r'^$', ProductListView.as_view()),
    url(r'^fbc/$', product_list_view),
    url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view()),
    url(r'^fbc/(?P<pk>\d+)/$', product_detail_view),
    url(r'^featured/$', ProductFeaturedListView.as_view()),
    url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),
]
