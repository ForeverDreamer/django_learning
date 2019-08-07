from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(request, "home_page.html", {})


def home_page_old(request):
    return HttpResponse("<h1>Hello World!</h1>")
