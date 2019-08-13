from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import Http404

from .models import Product
from carts.models import Cart


class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self):
        return Product.objects.all().featured()


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "products/featured-detail.html"

    # def get_queryset(self):
    #     return Product.objects.featured()


class ProductListView(ListView):
    # queryset = Product.objects.all()
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        # print(context)
        return context

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Product.objects.all()


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    print(queryset)
    return render(request, "products/list.html", context)


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')

        # instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found..")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Uhhmmm ")
        return instance


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        print(context)
        return context

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        obj = Product.objects.get_by_id(pk)
        if obj is None:
            raise Http404("Product doesn't exist")
        return obj

    # def get_queryset(self):
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)


def product_detail_view(request, pk, *arg, **kwargs):
    # obj = Product.objects.get(pk=pk)

    # obj = get_object_or_404(Product, pk=pk)

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

    obj = Product.objects.get_by_id(pk)
    if obj is None:
        raise Http404("Product doesn't exist")

    context = {
        'object': obj
    }
    print(obj)
    return render(request, "products/detail.html", context)
