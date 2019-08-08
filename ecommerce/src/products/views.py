from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import Http404

from .models import Product


# Create your views here.
class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        print(context)
        return context


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    print(queryset)
    return render(request, "products/list.html", context)


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        print(context)
        return context


def product_detail_view(request, pk, *arg, **kwargs):
    # obj = Product.objects.get(pk=pk)

    obj = get_object_or_404(Product, pk=pk)

    # try:
    #     obj = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print('no product here')
    #     raise Http404("Product doesn't exist")
    # except:
    #     print("huh?")

    # qs = Product.objects.filter(id=pk)
    # if qs.exists() and qs.count() == 1:  # len(qs)
    #     obj = qs.first()
    # else:
    #     raise Http404("Product doesn't exist")

    context = {
        'object': obj
    }
    print(obj)
    return render(request, "products/detail.html", context)
