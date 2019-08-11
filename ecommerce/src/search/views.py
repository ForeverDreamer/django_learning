from django.views.generic import ListView

from products.models import Product


class SearchProductView(ListView):
    template_name = "products/list.html"

    def get_queryset(self):
        """
            __icontains = field contains this
            __iexact = fields is exactly this
        """
        request = self.request
        method_dict = request.GET
        print(method_dict)
        query = method_dict.get('q', None)  # method_dict['q']
        print(query)
        if query is not None:
            return Product.objects.filter(title__icontains=query)
        return Product.objects.featured()
