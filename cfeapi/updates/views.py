from django.http import JsonResponse, HttpResponse

import json


# Create your views here.
# def detial_view(request):
# return render(request, template, {}) # return JSON data  --> JS Object Notion
# return HttpResponse(get_template().render({}))


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
    # return JsonResponse(data)
    return HttpResponse(json_data, content_type='application/json')
