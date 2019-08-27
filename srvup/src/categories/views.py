from django.views.generic import (
    DetailView,
    ListView
)

from .models import Category


class CategoryListView(ListView):
    queryset = Category.objects.all()


class CategoryDetailView(DetailView):
    queryset = Category.objects.all()
