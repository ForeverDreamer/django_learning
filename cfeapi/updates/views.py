from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


# Create your views here.
# def detial_view(request):
# return render(request, template, {}) # return JSON data  --> JS Object Notion
# return HttpResponse(get_template().render({}))


def json_example_view(request):
    """
    URI -- for a REST API
    """
    data = {
        "count": 1000,
        "content": "Some new content"
    }
    return JsonResponse(data)
