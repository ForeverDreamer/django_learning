from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from django.core.serializers import serialize

import json

from cfeapi.mixins import JsonResponseMixin
from .models import Update


# Create your views here.
# def detial_view(request):
#     return render(request, template, {}) # return JSON data  --> JS Object Notion
#     return HttpResponse(get_template().render({}))

# obj = Update.objects.get(id=1)

def json_example_view(request):
    """
    URI -- for a REST API
    GET -- Retrieve
    """
    data = {
        "count": 1000,
        "content": "Some new content"
    }
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content"
        }
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content"
        }
        return self.render_to_json_response(data)


class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        json_data = qs.serialize()
        return HttpResponse(json_data, content_type='application/json')

