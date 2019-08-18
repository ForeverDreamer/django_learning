from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.utils.http import is_safe_url

import stripe

STRIPE_PUB_KEY = getattr(settings, "STRIPE_PUB_KEY")
STRIPE_SECRET_KEY = getattr(settings, "STRIPE_SECRET_KEY")
stripe.api_key = STRIPE_SECRET_KEY


def payment_method_view(request):
    next_url = None
    next_ = request.GET.get('next')
    if is_safe_url(next_, request.get_host()):
        next_url = next_

    return render(request, 'billing/payment-method.html', {'public_key': STRIPE_PUB_KEY, "next_url": next_url})


def payment_method_createview(request):
    if request.method == 'POST':
        print(request.POST)
        return JsonResponse({'message': 'Done'})
    return HttpResponse('error', status_code=401)
