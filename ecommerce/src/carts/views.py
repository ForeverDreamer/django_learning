from django.shortcuts import render


def cart_home(request):
    print(dir(request.session))
    return render(request, "carts/home.html")
