from django.views.generic import (
    DetailView,
    ListView
)

from .models import Category


class CategoryListView(ListView):
    queryset = Category.objects.all().order_by('title')


class CategoryDetailView(DetailView):
    queryset = Category.objects.all()
