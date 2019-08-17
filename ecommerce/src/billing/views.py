from django.shortcuts import render
from django.conf import settings

import stripe

STRIPE_PUB_KEY = getattr(settings, "STRIPE_PUB_KEY")
STRIPE_SECRET_KEY = getattr(settings, "STRIPE_SECRET_KEY")
stripe.api_key = STRIPE_SECRET_KEY


def payment_method_view(request):
    if request.method == 'POST':
        print(request.POST)

    return render(request, 'billing/payment-method.html', {'public_key': STRIPE_PUB_KEY})
